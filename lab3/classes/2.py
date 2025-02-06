#Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        self.area = 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def getLength(self):
        self.length = int(input("Side: "))
    def calculateArea(self):
        self.area = self.length * self.length
        return self.area
a = Square(0)
a.getLength()
print("Area:", a.calculateArea())