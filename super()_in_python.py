
class Shape:
    def __init__(self, name, colour, is_filled):
        self.Name = name
        self.Colour = colour
        self.is_filled = is_filled   
    
    def describe(self):
        print(f"The {self.Name} is {self.Colour} and is {'Filled' if self.is_filled else 'not filled'}")



class Circle(Shape):
    def __init__(self, name, colour , is_filled, radius):
        super().__init__(name , colour, is_filled)
        self.Radius = radius

#   def describe(self):



class Square(Shape):
    def __init__(self, name, colour , is_filled, side):
        super().__init__(name , colour, is_filled)
        self.Side = side

    def describe(self):
        super().describe()
        print(f"The area of the {self.Name} is {self.Side * self.Side}")

    
class Triangle(Shape):
    def __init__(self, name,colour ,  is_filled,height, width):
        super().__init__(name , colour, is_filled)
        self.Height = height
        self.Width = width

    def describe(self):
        super().describe()
        print(f"The area of the {self.Name} is {self.Height * self.Width * 0.5}")


circle = Circle(name = "Circle" , colour = "Red" , radius = 5 , is_filled = False)
square = Square("Square" , "Blue" , True , 7)
triangle = Triangle("Triangle" , "Green" , False , 27 , 53)

print(circle.Radius)
square.describe()