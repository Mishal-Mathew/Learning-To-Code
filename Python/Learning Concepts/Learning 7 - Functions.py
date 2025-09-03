def sum(*args):  #args is a tuple 
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum(5,2)
print(result)

def address(**kwargs):  #kwargs is a dictionary
    for key,value in kwargs.items():
        print(f"{key} : {value}")

store = address(F_name="Mishal",
                L_name="Mathew")