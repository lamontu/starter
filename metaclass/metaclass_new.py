
class MetaCls1(type):
    def __new__(cls, name, bases, dct):
        # return a new type named "name",this type has nothing
        # to do with MetaCls,and MetaCl.__init__ won't be invoked
        return type(name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('MetaCls1.__init__')

class MetaCls2(type):
    def __new__(cls, name, bases, dct):
        # return a new type named "name",the returned type
        # is an instance of cls,and cls here is "MetaCls", so
        # the next step can invoke MetaCls.__init__
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('MetaCls2.__init__')

class A(metaclass=MetaCls1):
    pass

class B(metaclass=MetaCls2):
    pass

