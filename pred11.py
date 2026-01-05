#Point, [x, y], id
class Point:
    counter = 0
    def __init__(self, x=0, y=0):
        Point.counter = Point.counter + 1
        self.__id = Point.counter
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
        
    @property    
    def y(self):
        return self.__y
    
    @x.setter
    def y(self, y):
        self.__y = y
        
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
    
    def length(self, l):
        return self.distance2(l.s, l.e)
   

p1 = Point()
p1.print()
p2 = Point(10, 10)
p2.print()
p3 = Point(20, 20)
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

#Composition
class Line:
    def __init__(self, s, e):
        self.__s = s
        self.__e = e
        
    def print(self):
        print('Line:')
        self.__s.print()
        self.__e.print()
        
    @property    
    def s(self):
        return self.__s
    
    @s.setter
    def s(self, s):
        self.__s = s
        
    @property    
    def e(self):
        return self.__e
    
    @e.setter
    def e(self, e):
        self.__e = e
        
#Composition
class PolyLine:
    def __init__(self, *points):
        self.__points = points
        
    def print(self):
        print('Polyline:')
        for p in self.__points:
            p.print()
            
    @property    
    def points(self):
        return self.__points

#Create endpoints 
s = Point(0, 0)
e = Point(10, 10)

#Create line
line = Line(s, e)
line.print()

#Compute length
length = a.length(line)
print(length)

#Create polyline
p3 = Point(0, 10)
pol = PolyLine(p1, p2, p3)
pol.print()

#Graphical object
class GO:
    def __init__(self, color, style):
        self.__color = color
        self.__style = style
        
    @property    
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
        
    @property    
    def style(self):
        return self.__style
    
    @style.setter
    def style(self, style):
        self.__style = style
        
    def print(self):
        print ('GO')
        print(self.color, self.__style)
        

class PointGO(GO, Point):
    def __init__(self, color, style, x = 0, y = 0):
        #GO.__init__(color, style)
        #Point.__init__(x, y)
        super().__init__(color, style)
        super().__init__(x, y)
        
class LineGO(GO):
    def __init__(self, color, style, s, e):
        super().__init__(color, style)
        self.__s = s
        self.__e = e
        
    def print(self):
        print('Line G:')
        super().print()
        self.__s.print()
        self.__e.print()
        
    @property    
    def s(self):
        return self.__s
    
    @s.setter
    def s(self, s):
        self.__s = s
        
#Graphical object
go = GO(1, 2)

#Graphical point
pg1 = PointGO(1, 2, 0, 0)
pg2 = PointGO(3, 4, 10, 10)

#Graphical line
p1 = PointGO(0, 0)
p2 = PointGO(10, 10)
lineg = LineGO(5, 6, p1, p2)