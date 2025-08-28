#List comprehension

#    doubles =[]                                    
#    for i in range(1,11):
#        doubles.append(i * 2)        ==> Same as    
#    print(doubles)

doubles = [i * 2 for i in range(1,11)]
num = [i * 3 for i in range(1,11) if i % 2 == 0]
print(doubles)
print()
print(num)

#Switch statements

def number(num):
    match num:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4 | 5:
            return "Four or five"
        case _:
            return"Invalid"

print(number(5))