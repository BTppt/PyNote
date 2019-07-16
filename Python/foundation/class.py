# Class

## Definition
### class variables and instance variables
class Polygon:
    xpos = 0
    ypos = 0

    def __init__(self, vertex, angles):
        self.__vertex__ = vertex
        self.__angles__ = angles

    def vertexnum(self):
        return self.__vertex__

    # static method
    @staticmethod
    def count(self):
        self.xpos += 1


polygon1 = Polygon(3, [60, 60, 60])
polygon2 = Polygon(4, (90, 90, 90, 90))
polygon1.xpos = 4
print(polygon2.xpos)
Polygon.xpos = 8
print(polygon1.xpos)
print(polygon2.xpos)
# invoking instance method using class name
print(Polygon.vertexnum(polygon1))
# invoking static method
Polygon.count(polygon1)
print(polygon1.xpos)
del Polygon.xpos
# print(Polygon.xpos) >>AttributeError: type object 'Polygon' has no attribute 'xpos'

## Inheritance and derive
class Rect(Polygon):
    def __init__(self, vertex, angles):
        super(Rect, self).__init__(vertex, angles)
        self.xpos = 1
        self.ypos = 2

rect1 = Rect(4, [90, 90, 90, 90])
print(rect1.xpos)
print(rect1.ypos)