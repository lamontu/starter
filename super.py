class Foo(object):
    def bar(self, message):
        print(message)

a = Foo()
a.bar('Foo object say: Hello, world.')
print()

class FooParent(object):
    def bar(self, message):
        print(message)
'''
class FooChild(FooParent):
    def bar(self, message):
        FooParent.bar(self, message)
'''

class FooChild(FooParent):
    def bar(self, message):
        super(FooChild, self).bar(message)

b = FooChild()
b.bar('FooChild object say: Hello, world.')
