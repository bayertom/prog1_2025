#Point, [x, y]
class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        
    def print(self):
        print(self.__x, self.__y)
    
#Default initializer    
p1 = Point()
p1.print()
p2 = Point()
p2.print()

#Point, [x, y], default values
class Point2:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    def print(self):
        print(self.__x, self.__y)

#Initializer with parameters    
p1 = Point2()
p1.print()
p2 = Point2(10, 10)
p2.print()
p3 = Point2(20, 20)
p3.print()

#Point, [x, y], id, wrong
class Point3:
    id = 0
    def __init__(self, x=0, y=0):
        Point3.id = Point3.id + 1
        self.__x = x
        self.__y = y
        
    def print(self):
        print(self.__id , self.__x, self.__y)


p1 = Point3()
p1.print()
p2 = Point3(10, 10)
p2.print()
p3 = Point3(20, 20)
p3.print()
p1.print()    #ID changes, wrong

#Point, [x, y], id
class Point4:
    counter = 0
    def __init__(self, x=0, y=0):
        Point4.counter = Point4.counter + 1
        self.__id = Point4.counter
        self.__x = x
        self.__y = y
        
    def print(self):
        print(self.__id , self.__x, self.__y)
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    @property    
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

#Algprithms
class Algoritms:
    
    def distance(p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        
        return (dx*dx + dy*dy)**0.5
    
    def distance2(self, p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        
        return (dx*dx + dy*dy)**0.5

#OK  
p1 = Point4()
p1.print()
p2 = Point4(10, 10)
p2.print()
p3 = Point4(20, 20)
p3.print()
p1.print()
p1.x = 27
p1.print()

#Getter, setter
x1 = p1.getX()
p1.setX(8)
p1.print()

#Property
x2 = p1.x
p1.x = 25
p1.print()

#Passing objects + static call
d1 = Algoritms.distance(p1, p2)

#Passing objects + call
a = Algoritms()
d2 = a.distance2(p1, p2)