"""
MDC Mock

This probably isn't necessary since we should be able to actually use the real
java SLF4J package, but I just haven't figured out how to easily install that
for use in jython, and adding this here was the simplest way to let mes lib
tests run

"""

__all__ = [
    'get'
]


def get(key):
    return None

