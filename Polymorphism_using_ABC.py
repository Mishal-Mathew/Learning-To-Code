
import abc 

class shape(abc):
    @abstractmethod
    def area(self):
        pass

class circle(shape):

    def __init__(self , radius):
        self.r = radius
    
    def area(self):
        return 3.14 * self.r ** 2
    
class square(shape):
    def __init__(self , side):
        self.s = side
    
    def area(self):
        return self.s ** 2 

class triangle(shape):
    def __init__(self , base , height):
        self.b = base 
        self.h = height
    
    def area(self):
        return self.b * self.h * 0.5

class pizza(circle):
    def __init__(self , topping , radius):
        super().__init__(radius)
        self.top = topping

shapes = [circle(5) , square(6) , triangle(3,4), pizza("Pineapple" , 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")
