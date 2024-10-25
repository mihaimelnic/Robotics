;; Auto-generated. Do not edit!


(when (boundp 'locobot_simulation::ObjectInfo)
  (if (not (find-package "LOCOBOT_SIMULATION"))
    (make-package "LOCOBOT_SIMULATION"))
  (shadow 'ObjectInfo (find-package "LOCOBOT_SIMULATION")))
(unless (find-package "LOCOBOT_SIMULATION::OBJECTINFO")
  (make-package "LOCOBOT_SIMULATION::OBJECTINFO"))

(in-package "ROS")
;;//! \htmlinclude ObjectInfo.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass locobot_simulation::ObjectInfo
  :super ros::object
  :slots (_name _color _size _pose ))

(defmethod locobot_simulation::ObjectInfo
  (:init
   (&key
    ((:name __name) "")
    ((:color __color) "")
    ((:size __size) 0.0)
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _color (string __color))
   (setq _size (float __size))
   (setq _pose __pose)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:color
   (&optional __color)
   (if __color (setq _color __color)) _color)
  (:size
   (&optional __size)
   (if __size (setq _size __size)) _size)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; string _color
    4 (length _color)
    ;; float64 _size
    8
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string _color
       (write-long (length _color) s) (princ _color s)
     ;; float64 _size
       (sys::poke _size (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _size
     (setq _size (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get locobot_simulation::ObjectInfo :md5sum-) "7e7793172c4fe3744410cf6fe4cfc055")
(setf (get locobot_simulation::ObjectInfo :datatype-) "locobot_simulation/ObjectInfo")
(setf (get locobot_simulation::ObjectInfo :definition-)
      "string name
string color
float64 size
geometry_msgs/Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :locobot_simulation/ObjectInfo "7e7793172c4fe3744410cf6fe4cfc055")


