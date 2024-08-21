#WAP using oop to calculate the area and circumference of a circle

class Circle:
  pie = 3.14
  def __init__(self,lenght, width):
    self.lenght = lenght
    self.width = width
  def area(self):
    print(self.lenght * self.width);
    
  def circumfrence(self, raduis):
    print(Circle.pie * raduis** 2)
    

circle1 = Circle(20, 10)
print(circle1.width)
circle1.area()
circle1.circumfrence(4)
