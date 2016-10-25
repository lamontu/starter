class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    area = property(getArea, doc = 'area of the rectangle')

a = Rect(2, 3)

print('a.area:')
a.area
print()

print('a.area = 3')
a.area = 3
