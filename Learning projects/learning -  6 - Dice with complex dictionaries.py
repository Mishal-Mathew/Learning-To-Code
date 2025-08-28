import random 

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")
#● ┌ ─ ┐ │ └ ┘ 
 
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘" 

dice_collect={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"),}

dice=[]
total = 0
user_num= int(input("How many dice? :"))

for i in range(user_num):
    dice.append(random.randint(1,6))
print(dice)

#for i in range(user_num):
#    for j in dice_collect.get(dice[i]):
#        print(j)

for i in range(5):
    for j in dice:
        print(dice_collect.get(j)[i],end="")
    print()
       
for i in dice:
    total += i  
print(f"The total is {total}")