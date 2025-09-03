
def add_sprinkles(func):
    def wrapper(*args , **kwargs):
        print("Sprinkles has been added")
        func(*args , **kwargs)
    return wrapper

def add_brownie(func):
    def wrapper(*args , **kwargs):
        print("Brownie has been added")
        func(*args , **kwargs)
    return wrapper


@add_sprinkles
@add_brownie
def ice_cream(flavour,scoops):
    print(f"Here is your {scoops} scoops of {flavour} ice cream")

ice_cream(scoops = 3,flavour = "Vanilla")

