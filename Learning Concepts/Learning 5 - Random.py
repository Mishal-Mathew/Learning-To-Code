import random as ran

#num = ran.randint(1,20)
#fnum = ram.random()
#option= ram.choice(options)
#cards = ram.shuffle(deck)

guesses = 0
print(f"Python Number Guessing Game")
rand = ran.randint(1,100)
print("Select a number between 1 and 100")
while True:
    guesses += 1
    print()
    user_num = input("Enter your guess : ")
    if user_num.isdigit() == True:
        user_num = int(user_num)
        if user_num < 1 or user_num > 100:
            print("That number is out of range.Please try again")
        elif user_num == rand:
            print("CONGRATS!!You have found the number!!")
            print(f"No of guesses:{guesses}")
            break
        elif user_num < rand:
            print("Too low!.Try again")
        else:
            print("Too high!.Try again")
    else:
        print("Invalid guess")