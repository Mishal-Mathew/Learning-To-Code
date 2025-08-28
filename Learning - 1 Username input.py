name = input("Enter your name :")
if len(name)>12:
    print("Invalid username - The username should not exceed 12 letters")
elif name.isalpha() == False:
    print("Invalid username - The username should only contain letters")
else:
    print(name)