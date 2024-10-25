; Auto-generated. Do not edit!


(cl:in-package locobot_simulation-msg)


;//! \htmlinclude ObjectInfos.msg.html

(cl:defclass <ObjectInfos> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (detected_objects
    :reader detected_objects
    :initarg :detected_objects
    :type (cl:vector locobot_simulation-msg:ObjectInfo)
   :initform (cl:make-array 0 :element-type 'locobot_simulation-msg:ObjectInfo :initial-element (cl:make-instance 'locobot_simulation-msg:ObjectInfo))))
)

(cl:defclass ObjectInfos (<ObjectInfos>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectInfos>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectInfos)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name locobot_simulation-msg:<ObjectInfos> is deprecated: use locobot_simulation-msg:ObjectInfos instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ObjectInfos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locobot_simulation-msg:header-val is deprecated.  Use locobot_simulation-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'detected_objects-val :lambda-list '(m))
(cl:defmethod detected_objects-val ((m <ObjectInfos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader locobot_simulation-msg:detected_objects-val is deprecated.  Use locobot_simulation-msg:detected_objects instead.")
  (detected_objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectInfos>) ostream)
  "Serializes a message object of type '<ObjectInfos>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'detected_objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'detected_objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectInfos>) istream)
  "Deserializes a message object of type '<ObjectInfos>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'detected_objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'detected_objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'locobot_simulation-msg:ObjectInfo))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectInfos>)))
  "Returns string type for a message object of type '<ObjectInfos>"
  "locobot_simulation/ObjectInfos")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectInfos)))
  "Returns string type for a message object of type 'ObjectInfos"
  "locobot_simulation/ObjectInfos")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectInfos>)))
  "Returns md5sum for a message object of type '<ObjectInfos>"
  "1324374ccaec257e2f70fe89faafdce9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectInfos)))
  "Returns md5sum for a message object of type 'ObjectInfos"
  "1324374ccaec257e2f70fe89faafdce9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectInfos>)))
  "Returns full string definition for message of type '<ObjectInfos>"
  (cl:format cl:nil "std_msgs/Header header~%ObjectInfo[] detected_objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: locobot_simulation/ObjectInfo~%string name~%string color~%float64 size~%geometry_msgs/Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectInfos)))
  "Returns full string definition for message of type 'ObjectInfos"
  (cl:format cl:nil "std_msgs/Header header~%ObjectInfo[] detected_objects~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: locobot_simulation/ObjectInfo~%string name~%string color~%float64 size~%geometry_msgs/Pose pose~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectInfos>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'detected_objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectInfos>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectInfos
    (cl:cons ':header (header msg))
    (cl:cons ':detected_objects (detected_objects msg))
))
