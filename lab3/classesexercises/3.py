class Rectangle:
    def __init__(self, a, b):
        self.S = self.a * self.b
    
    def area(self):
        print(self.a * self.b)

class Shape(Rectangle):
    def __init__(self, a = 0, b = 0):
        Rectangle.a = a 
        Rectangle.b = b


p1 = Shape(5, 6)

p1.area()


