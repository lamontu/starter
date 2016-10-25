class C(object):
    def getX(self):
        print('get x')
        return self.__x
    def setX(self, value):
        print('set x', value)
        self.__x = value
    def delX(self):
        print('del x')
        del self.__x
    x = property(getX, setX, delX, "This is 'x' property.")

c = C()
print('c.x =1:')
c.x = 1
print()

print('t = c.x:')
t = c.x
print('t =', t)
print()

print('del c.x:')
del c.x
print()

print('C.x: ', C.x)
