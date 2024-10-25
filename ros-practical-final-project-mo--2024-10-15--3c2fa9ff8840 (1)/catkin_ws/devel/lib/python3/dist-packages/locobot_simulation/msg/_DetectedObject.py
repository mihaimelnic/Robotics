# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from locobot_simulation/DetectedObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class DetectedObject(genpy.Message):
  _md5sum = "24b1559ff07fbef77b52a17ccdb9e43a"
  _type = "locobot_simulation/DetectedObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string name
string label
float64 probability
int64[] bbox
std_msgs/ColorRGBA color
geometry_msgs/Point position
int32 num_points
================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['name','label','probability','bbox','color','position','num_points']
  _slot_types = ['string','string','float64','int64[]','std_msgs/ColorRGBA','geometry_msgs/Point','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,label,probability,bbox,color,position,num_points

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DetectedObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.label is None:
        self.label = ''
      if self.probability is None:
        self.probability = 0.
      if self.bbox is None:
        self.bbox = []
      if self.color is None:
        self.color = std_msgs.msg.ColorRGBA()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.num_points is None:
        self.num_points = 0
    else:
      self.name = ''
      self.label = ''
      self.probability = 0.
      self.bbox = []
      self.color = std_msgs.msg.ColorRGBA()
      self.position = geometry_msgs.msg.Point()
      self.num_points = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.label
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.probability
      buff.write(_get_struct_d().pack(_x))
      length = len(self.bbox)
      buff.write(_struct_I.pack(length))
      pattern = '<%sq'%length
      buff.write(struct.Struct(pattern).pack(*self.bbox))
      _x = self
      buff.write(_get_struct_4f3di().pack(_x.color.r, _x.color.g, _x.color.b, _x.color.a, _x.position.x, _x.position.y, _x.position.z, _x.num_points))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.color is None:
        self.color = std_msgs.msg.ColorRGBA()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.label = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.label = str[start:end]
      start = end
      end += 8
      (self.probability,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sq'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.bbox = s.unpack(str[start:end])
      _x = self
      start = end
      end += 44
      (_x.color.r, _x.color.g, _x.color.b, _x.color.a, _x.position.x, _x.position.y, _x.position.z, _x.num_points,) = _get_struct_4f3di().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.label
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.probability
      buff.write(_get_struct_d().pack(_x))
      length = len(self.bbox)
      buff.write(_struct_I.pack(length))
      pattern = '<%sq'%length
      buff.write(self.bbox.tostring())
      _x = self
      buff.write(_get_struct_4f3di().pack(_x.color.r, _x.color.g, _x.color.b, _x.color.a, _x.position.x, _x.position.y, _x.position.z, _x.num_points))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.color is None:
        self.color = std_msgs.msg.ColorRGBA()
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.label = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.label = str[start:end]
      start = end
      end += 8
      (self.probability,) = _get_struct_d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sq'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.bbox = numpy.frombuffer(str[start:end], dtype=numpy.int64, count=length)
      _x = self
      start = end
      end += 44
      (_x.color.r, _x.color.g, _x.color.b, _x.color.a, _x.position.x, _x.position.y, _x.position.z, _x.num_points,) = _get_struct_4f3di().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4f3di = None
def _get_struct_4f3di():
    global _struct_4f3di
    if _struct_4f3di is None:
        _struct_4f3di = struct.Struct("<4f3di")
    return _struct_4f3di
_struct_d = None
def _get_struct_d():
    global _struct_d
    if _struct_d is None:
        _struct_d = struct.Struct("<d")
    return _struct_d
