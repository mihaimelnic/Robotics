# Locobot Manipulator: A Robotics AI Approach by Group 16

## 1. Description
This project focuses on controlling a LocoBot manipulator to sort various objects based on their color and size. It includes scripts for object detection, robotic manipulation, and camera control, with the overall aim of sorting objects into designated areas.

## 2. Getting Started
This project utilizes ROS (Robot Operating System) and is developed within an online environment on theappconstruct.ai. This environment provides the necessary server connection, a virtual Visual Studio Code machine, and includes MoveIt, Gazebo, and other essential resources for running the simulation.

### 2.1 Dependencies

- **Operating System**: Windows 10 or higher (or compatible Linux systems)
- **Python Version**: Python 3.7 or higher
- **Visual Studio Code** (recommended)
- **Required Libraries**:
  - `opencv-python`
  - `rospy`
  - `numpy`
  - `matplotlib`

### 2.2 Installation
Ensure ROS and MoveIt are installed on the server or machine where this project is deployed. The code relies on a simulation environment, so make sure all ROS packages, including `locobot_moveit` and `locobot_simulation`, are properly configured. 

## 3. Code Overview

### 3.1 Added Scripts
- **sorting.py**: Controls the LocoBot manipulator to pick up objects detected by the perception node and place them into designated areas based on color.
- **detection.py**: Detects objects by color and size using the robot's camera, publishing details and providing an annotated image for debugging.
- **get_joint_val.py**: Retrieves and prints current joint values of the robot’s arm.
- **move_to_pose.py**: Moves the robot's arm to a predefined pose.
- **point_head.py**: Controls the camera's pan and tilt angles, adjusting it to look in specified directions.

### 3.2 Custom Messages
- **ObjectInfo.msg**: A custom ROS message format used for publishing detected object information, including size, color, and pose.

### 3.3 Launch Files
- **perception.launch**: Initializes the `detection.py` node with specified parameters for input images, detection outputs, and annotated images.
- **sorting.launch**: Starts the `sorting.py` script for the sorting task.

## 4. Running the Project

To run the project, follow these steps:

1. **Start the Simulation with MoveIt:**
   ```bash
   roslaunch locobot_moveit xslocobot_moveit.launch

## 5. Authors

Members of group 16: Ionut-Valentin Moise, Cezar Casian Solovastru, Vlad Morar, Melnic Mihaita-Nicusor

Work done under VU Bachelors Courses
## 6. Version History
* 0.1
    * Initial Release - October 2024. 

