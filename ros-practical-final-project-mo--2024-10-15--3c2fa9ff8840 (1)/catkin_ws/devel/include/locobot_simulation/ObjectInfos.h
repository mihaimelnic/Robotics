// Generated by gencpp from file locobot_simulation/ObjectInfos.msg
// DO NOT EDIT!


#ifndef LOCOBOT_SIMULATION_MESSAGE_OBJECTINFOS_H
#define LOCOBOT_SIMULATION_MESSAGE_OBJECTINFOS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <locobot_simulation/ObjectInfo.h>

namespace locobot_simulation
{
template <class ContainerAllocator>
struct ObjectInfos_
{
  typedef ObjectInfos_<ContainerAllocator> Type;

  ObjectInfos_()
    : header()
    , detected_objects()  {
    }
  ObjectInfos_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , detected_objects(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::locobot_simulation::ObjectInfo_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::locobot_simulation::ObjectInfo_<ContainerAllocator> >::other >  _detected_objects_type;
  _detected_objects_type detected_objects;





  typedef boost::shared_ptr< ::locobot_simulation::ObjectInfos_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::locobot_simulation::ObjectInfos_<ContainerAllocator> const> ConstPtr;

}; // struct ObjectInfos_

typedef ::locobot_simulation::ObjectInfos_<std::allocator<void> > ObjectInfos;

typedef boost::shared_ptr< ::locobot_simulation::ObjectInfos > ObjectInfosPtr;
typedef boost::shared_ptr< ::locobot_simulation::ObjectInfos const> ObjectInfosConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::locobot_simulation::ObjectInfos_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::locobot_simulation::ObjectInfos_<ContainerAllocator1> & lhs, const ::locobot_simulation::ObjectInfos_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.detected_objects == rhs.detected_objects;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::locobot_simulation::ObjectInfos_<ContainerAllocator1> & lhs, const ::locobot_simulation::ObjectInfos_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace locobot_simulation

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::locobot_simulation::ObjectInfos_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::locobot_simulation::ObjectInfos_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::locobot_simulation::ObjectInfos_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1324374ccaec257e2f70fe89faafdce9";
  }

  static const char* value(const ::locobot_simulation::ObjectInfos_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1324374ccaec257eULL;
  static const uint64_t static_value2 = 0x2f70fe89faafdce9ULL;
};

template<class ContainerAllocator>
struct DataType< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "locobot_simulation/ObjectInfos";
  }

  static const char* value(const ::locobot_simulation::ObjectInfos_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n"
"ObjectInfo[] detected_objects\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: locobot_simulation/ObjectInfo\n"
"string name\n"
"string color\n"
"float64 size\n"
"geometry_msgs/Pose pose\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::locobot_simulation::ObjectInfos_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.detected_objects);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ObjectInfos_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::locobot_simulation::ObjectInfos_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::locobot_simulation::ObjectInfos_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "detected_objects[]" << std::endl;
    for (size_t i = 0; i < v.detected_objects.size(); ++i)
    {
      s << indent << "  detected_objects[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::locobot_simulation::ObjectInfo_<ContainerAllocator> >::stream(s, indent + "    ", v.detected_objects[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // LOCOBOT_SIMULATION_MESSAGE_OBJECTINFOS_H