
__all__ = [
    'readValue',
    'readValues',
    'writeValue',
    'writeValues',

    "Quality",
    "QualifiedValue"
]

def readValue(opcServer, itemPath):
    return QualifiedValue()

def readValues(opcServer, itemPaths):
    print(opcServer, itemPaths)
    return [QualifiedValue()]

def writeValue(opcServer, itemPath, value):
    """Writes a value directly through an OPC server connection
    synchronously. Will return an OPC-UA status code object. You can
    quickly check if the write succeeded by calling isGood() on the
    return value from this function.
    Args:
        opcServer (str): The name of the OPC server connection in
            which the item resides.
        itemPath (str): The item path, or address, to write to.
        value (object): The value to write to the OPC item.
    Returns:
        Quality: The status of the write. Use returnValue.isGood() to
            check if the write succeeded.
    """
    print(opcServer, itemPath, value)
    return Quality()

def writeValues(opcServer, itemPaths, values):

    print(opcServer, itemPaths, values)
    return [Quality()]

class QualifiedValue(object):
    """QualifiedValue class"""

    def __init__(self, value=None, quality=None, timestamp=None):
        self.value = value
        self.quality = quality
        self.timestamp = timestamp

class Quality(object):
    """QualifiedValue class"""

    def __init__(self, is_good=True):
        self.is_good = is_good

    def isGood(self):
        return self.is_good
