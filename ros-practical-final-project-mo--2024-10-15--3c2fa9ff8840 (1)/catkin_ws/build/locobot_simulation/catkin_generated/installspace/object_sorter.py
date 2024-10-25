#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import tf
import math
from locobot_simulation.msg import BoundingBoxes, BoundingBox
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Image, CameraInfo

class ObjectSorter:
    def __init__(self):
        # Initialize MoveIt and ROS node
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('object_sorter', anonymous=True)

        # Initialize RobotCommander, PlanningSceneInterface, and MoveGroupCommanders with namespaces and robot descriptions
        robot_description = "locobot/robot_description"
        ns = "/locobot"

        self.robot = moveit_commander.RobotCommander(robot_description, ns)
        self.scene = moveit_commander.PlanningSceneInterface(ns)

        # Move group for the arm
        self.group_name = "interbotix_arm"
        self.move_group = moveit_commander.MoveGroupCommander(self.group_name, robot_description, ns)

        # Move group for the gripper
        self.gripper_group_name = "interbotix_gripper"
        self.gripper_group = moveit_commander.MoveGroupCommander(self.gripper_group_name, robot_description, ns)

        # Publisher to display trajectories in RViz
        self.display_trajectory_publisher = rospy.Publisher(
            '/move_group/display_planned_path',
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=1
        )

        # TF listener
        self.tf_listener = tf.TransformListener()

        # Subscribe to detection topic
        self.detection_sub = rospy.Subscriber(
            '/yolov5/BoundingBoxes', BoundingBoxes, self.detection_callback
        )

        # Camera info subscriber (for depth information)
        self.depth_sub = rospy.Subscriber(
            '/locobot/camera/depth/image_raw', Image, self.depth_callback
        )

        # Depth image data
        self.depth_image = None

        # Camera info
        self.camera_info = None
        self.camera_info_sub = rospy.Subscriber(
            '/locobot/camera/depth/camera_info', CameraInfo, self.camera_info_callback
        )

        # Processed objects
        self.processed_objects = []

        # Gripper positions
        self.open_gripper_position = [0.04]  # Adjust based on your robot's gripper
        self.closed_gripper_position = [0.0]

        # Place positions
        self.x_red_mat = 0.5
        self.y_red_mat = 0.3
        self.x_blue_mat = 0.5
        self.y_blue_mat = -0.3
        self.z_place_height = 0.1

    def camera_info_callback(self, data):
        self.camera_info = data

    def depth_callback(self, data):
        # Store depth image data
        self.depth_image = data

    def detection_callback(self, data):
        bounding_boxes = data.bounding_boxes
        for box in bounding_boxes:
            class_name = box.Class
            if class_name in self.processed_objects:
                continue  # Skip already processed objects
            if self.is_graspable(class_name):
                # Get object's 3D position
                object_pose = self.get_3d_position(box)
                if object_pose:
                    color = self.get_color_from_name(class_name)
                    self.pick_and_place(class_name, object_pose, color)
                    self.processed_objects.append(class_name)

    def is_graspable(self, class_name):
        graspable_objects = [
            'red_cube', 'blue_cube', 'red_ball', 'blue_ball', 'red_cylinder', 'blue_cylinder']
        return class_name in graspable_objects

    def get_color_from_name(self, class_name):
        if 'red' in class_name:
            return 'red'
        elif 'blue' in class_name:
            return 'blue'
        else:
            return 'unknown'

    def get_3d_position(self, box):
        # Convert 2D bounding box to 3D pose using depth data
        if self.depth_image is None or self.camera_info is None:
            rospy.logwarn("No depth image or camera info available")
            return None

        # Extract center pixel
        u = int((box.xmin + box.xmax) / 2)
        v = int((box.ymin + box.ymax) / 2)

        # Get depth at center pixel
        import cv2
        from cv_bridge import CvBridge, CvBridgeError
        bridge = CvBridge()
        try:
            depth_image = bridge.imgmsg_to_cv2(self.depth_image, desired_encoding='passthrough')
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
            return None

        depth = depth_image[v, u]  # Depth in meters

        if depth == 0 or math.isnan(depth):
            rospy.logwarn("Depth at pixel (%d, %d) is invalid", u, v)
            return None

        # Convert (u, v, depth) to (x, y, z) in camera frame
        fx = self.camera_info.K[0]
        fy = self.camera_info.K[4]
        cx = self.camera_info.K[2]
        cy = self.camera_info.K[5]

        x = (u - cx) * depth / fx
        y = (v - cy) * depth / fy
        z = depth

        # Transform point to base_link frame
        point_in_camera = PoseStamped()
        point_in_camera.header.frame_id = 'locobot/camera_color_optical_frame'  # Adjust as per your setup
        point_in_camera.pose.position.x = x
        point_in_camera.pose.position.y = y
        point_in_camera.pose.position.z = z
        point_in_camera.pose.orientation.w = 1.0

        try:
            self.tf_listener.waitForTransform(
                'locobot/base_link', 'locobot/camera_color_optical_frame', rospy.Time(0), rospy.Duration(4.0))
            point_in_base = self.tf_listener.transformPose(
                'locobot/base_link', point_in_camera)
            return point_in_base.pose
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            rospy.logerr("TF Exception: %s", str(e))
            return None

    def pick_and_place(self, class_name, object_pose, color):
        # Adjust grasp pose
        grasp_pose = geometry_msgs.msg.Pose()
        grasp_pose.position = object_pose.position
        grasp_pose.position.z += 0.1  # Approach from above

        # Set orientation (end-effector pointing down)
        quat = tf.transformations.quaternion_from_euler(
            math.radians(180), 0, 0)
        grasp_pose.orientation.x = quat[0]
        grasp_pose.orientation.y = quat[1]
        grasp_pose.orientation.z = quat[2]
        grasp_pose.orientation.w = quat[3]

        rospy.loginfo("Picking up %s (%s)", class_name, color)

        # Move to pre-grasp pose
        self.move_group.set_pose_target(grasp_pose)
        success = self.move_group.go(wait=True)
        self.move_group.stop()
        self.move_group.clear_pose_targets()
        if not success:
            rospy.logerr("Failed to reach pre-grasp pose")
            return

        # Lower to grasp
        grasp_pose.position.z -= 0.1
        self.move_group.set_pose_target(grasp_pose)
        success = self.move_group.go(wait=True)
        self.move_group.stop()
        self.move_group.clear_pose_targets()
        if not success:
            rospy.logerr("Failed to reach grasp pose")
            return

        # Close the gripper
        self.close_gripper()

        # Lift up
        grasp_pose.position.z += 0.1
        self.move_group.set_pose_target(grasp_pose)
        success = self.move_group.go(wait=True)
        self.move_group.stop()
        self.move_group.clear_pose_targets()

        # Move to place location
        place_pose = geometry_msgs.msg.Pose()
        if color == 'red':
            place_pose.position.x = self.x_red_mat
            place_pose.position.y = self.y_red_mat
        elif color == 'blue':
            place_pose.position.x = self.x_blue_mat
            place_pose.position.y = self.y_blue_mat
        else:
            rospy.logerr("Unknown color")
            return
        place_pose.position.z = self.z_place_height
        place_pose.orientation = grasp_pose.orientation

        rospy.loginfo("Placing %s on %s mat", class_name, color)

        self.move_group.set_pose_target(place_pose)
        success = self.move_group.go(wait=True)
        self.move_group.stop()
        self.move_group.clear_pose_targets()
        if not success:
            rospy.logerr("Failed to reach place pose")
            return

        # Open the gripper
        self.open_gripper()

        # Retreat
        place_pose.position.z += 0.1
        self.move_group.set_pose_target(place_pose)
        self.move_group.go(wait=True)
        self.move_group.stop()
        self.move_group.clear_pose_targets()

    def open_gripper(self):
        gripper_joint_values = self.gripper_group.get_current_joint_values()
        gripper_joint_values[0] = self.open_gripper_position[0]
        self.gripper_group.set_joint_value_target(gripper_joint_values)
        self.gripper_group.go(wait=True)
        self.gripper_group.stop()

    def close_gripper(self):
        gripper_joint_values = self.gripper_group.get_current_joint_values()
        gripper_joint_values[0] = self.closed_gripper_position[0]
        self.gripper_group.set_joint_value_target(gripper_joint_values)
        self.gripper_group.go(wait=True)
        self.gripper_group.stop()

    def run(self):
        rospy.spin()


if __name__ == '__main__':
    try:
        sorter = ObjectSorter()
        sorter.run()
    except rospy.ROSInterruptException:
        pass
