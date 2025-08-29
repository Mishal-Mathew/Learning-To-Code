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
Dog.speak()


#This is multiple Inheritance


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):                         #Inheriting from Animal class
    def hunt(self):
        print(f"{self.name} is hunting")

class Deer(Prey):                    #Deer is inheriting from Prey ,which itself is inheriting from Animal
    def speak(self):
        print("Baa!")                   #This is multi-level

class Lion(Predator):
    pass

class Snake(Prey , Predator):         #Snake is inheriting from both Prey and Predator
    pass                                  # This is multiple 

Lion = Lion("Tiago")
Deer = Deer("Puerto Rico")
Pambu = Snake("Meme")

Pambu.hunt()
Pambu.flee()
Deer.speak()
try:
    Lion.flee()          #Lion can't flee because it is not inheriting from Prey class
except AttributeError as e:
    print(f"Error: {e} - Lion cannot flee because it does not inherit from Prey.")
