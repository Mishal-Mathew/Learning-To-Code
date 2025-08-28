#Object oriented programming in python

class Car:

    def __init__(self, model , colour , year):       #This is a constructor
        self.model = model
        self.colour =colour                          #These are attributes(variables) 
        self.ye = year
    
    def drive(self):                                 #These are methods(functions) 
        print(f"You drived {self.model}")

    def stop(self):
        print(f"You stopped {self.model}")

car1 = Car("BMW" , "Red" , 2007)            #These are the instances(objects)
car2 = Car("Porsche" , "Green", 1997)

print(car2.model)
print(car2.colour)
print(car2.ye)

car1.drive()
car2.drive()
car1.stop()
car2.stop()
