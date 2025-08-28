 #Concession stand program

menu = {"Pizza" : 3.00,
        "Nachos" : 4.50,
        "Popcorn" : 6.00}
cart = []
total = 0
print("------Menu------")
for key,value in menu.items():
    print(f"{key:8} : ${value:.2f}")
while True:
    food = input("Seclect an item(Q to quit)").capitalize()
    if food.upper()=="Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Not available")
print("-----Your Order-----")
print()
for food in cart:
    total += menu.get(food)
    print(food)
print()
print(f"Your total is ${total:.2f}")
         