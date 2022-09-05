class TestMetaClass(type):
    def __new__(mcs, *args, **kwargs):
        print('TestMetaClass.__new__', mcs)
        return type.__new__(mcs, *args, **kwargs)
    
    def __init__(cls, name, bases, kwds):
        print('TestMetaCalss.__init__', cls)
        super(TestMetaClass, cls).__init__(name, bases, kwds)
    
    def __call__(cls, *args, **kwargs):
        print('TestMetaClass.__call__', cls)
        return super(TestMetaClass, cls).__call__(*args, **kwargs)

class Foo(metaclass=TestMetaClass):
    yaml_tag = '!Foo'
    def __new__(cls, *args, **kwargs):
        print('Foo.__new__', cls)
        return super(Foo, cls).__new__(cls)
    
    def __init__(self, name=None):
        self.name = name
        print('Foo.__init__', self)

foo = Foo('hello')
print(foo.yaml_tag)
print(foo.name)
