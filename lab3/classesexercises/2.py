class Square:
    def __init__(self, len):
        self.len = len 
    
    def area(self):
        print(pow(self.len, 2))

class Shape(Square):
    def __init__(self, len = 0):
        Square.len = len 

p1 = Shape(5)
p1.area()



