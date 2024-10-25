;; Auto-generated. Do not edit!


(when (boundp 'locobot_simulation::ObjectInfos)
  (if (not (find-package "LOCOBOT_SIMULATION"))
    (make-package "LOCOBOT_SIMULATION"))
  (shadow 'ObjectInfos (find-package "LOCOBOT_SIMULATION")))
(unless (find-package "LOCOBOT_SIMULATION::OBJECTINFOS")
  (make-package "LOCOBOT_SIMULATION::OBJECTINFOS"))

(in-package "ROS")
;;//! \htmlinclude ObjectInfos.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass locobot_simulation::ObjectInfos
  :super ros::object
  :slots (_header _detected_objects ))

(defmethod locobot_simulation::ObjectInfos
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:detected_objects __detected_objects) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _detected_objects __detected_objects)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:detected_objects
   (&rest __detected_objects)
   (if (keywordp (car __detected_objects))
       (send* _detected_objects __detected_objects)
     (progn
       (if __detected_objects (setq _detected_objects (car __detected_objects)))
       _detected_objects)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; locobot_simulation/ObjectInfo[] _detected_objects
    (apply #'+ (send-all _detected_objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; locobot_simulation/ObjectInfo[] _detected_objects
     (write-long (length _detected_objects) s)
     (dolist (elem _detected_objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; locobot_simulation/ObjectInfo[] _detected_objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _detected_objects (let (r) (dotimes (i n) (push (instance locobot_simulation::ObjectInfo :init) r)) r))
     (dolist (elem- _detected_objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get locobot_simulation::ObjectInfos :md5sum-) "1324374ccaec257e2f70fe89faafdce9")
(setf (get locobot_simulation::ObjectInfos :datatype-) "locobot_simulation/ObjectInfos")
(setf (get locobot_simulation::ObjectInfos :definition-)
      "std_msgs/Header header
ObjectInfo[] detected_objects

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: locobot_simulation/ObjectInfo
string name
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



(provide :locobot_simulation/ObjectInfos "1324374ccaec257e2f70fe89faafdce9")


