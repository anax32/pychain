import struct


def type_to_bytearray(x):
  """
  convert any type into a byte array for block storage
  """
  cnvs = {
    bytes: lambda x: x,
    bytearray: lambda x: x,
    int: lambda x: bytearray(struct.pack("!i", x)),
    float: lambda x: bytearray(struct.pack("!f", x)),
    str: lambda x: x.encode(),
  }

  try:
    return cnvs[type(x)](x)
  except KeyError:
    logger.error("cannot convert type: '%s'[%s]" % (str(type(x)), str(x)))
