
try:
    user = int(input("Enter a number: ") )
    print(1/ user)

except ZeroDivisionError:
    print("Number can't be divided by zero")
except ValueError:
    print("The value should be a number")
except exceptions:
    print("Something went wrong")