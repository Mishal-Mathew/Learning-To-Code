#This is Inheritance


class Animal:

    def __init__(self  , name):

        self.name = name 
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):                               #Dog is inheriting from Animal class
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

Dog = Dog("Done")                                 # Don't forget the order🤓
Cat  = Cat("Rish")                                # Class---Constructor(if needed)---Method----Object
Cat.eat()


#This is multiple Inheritance


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):                         #Inheriting from Animal class
    def hunt(self):
        print(f"{self.name} is hunting")

class Deer(Prey):                    #Deer is inheriting from Prey ,which itself is inheriting from Animal
    pass                                 #This is multi-level               

class Lion(Predator):
    pass

class Snake(Prey , Predator):         #Snake is inheriting from both Prey and Predator
    pass                                  # This is multiple 

Lion = Lion("Tiago")
Deer = Deer("Puerto Rico")
Pambu = Snake("Meme")

Pambu.hunt()





