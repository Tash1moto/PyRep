class Singleton(object):
    __slots__ = ("__instance", )

def foo():
    return foo()
