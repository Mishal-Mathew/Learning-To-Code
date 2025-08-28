

class Rectangle:

    def __init__(self,width,height):
        self._width = width                 # _ mean private , it should be accessed in the class only ie it's raw
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Invalid number")

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Invalid number")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")



rectangle1 = Rectangle(3,4)

rectangle1.width = 4
rectangle1.height = 7

print(rectangle1.width)
print(rectangle1.height)

del rectangle1.width
del rectangle1.height

