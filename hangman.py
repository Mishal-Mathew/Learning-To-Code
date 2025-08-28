import random

options = ("whale" , "salmon" , "dolphin" , "shark" , "starfish", "snail")
hangman_arts = {0: ("     ",
                    "     ",
                    "     "),
                1: (" o   ",
                    "     ",
                    "     "),
                2: (" o   ",
                    " |   ",
                    "     "),
                3: (" o   ",
                    "/|   ",
                    "     "),
                4: (" o   ",
                    "/|\\ ",
                    "     "),
                5: (" o   ",
                    "/|\\ ",
                    "/    "),
                6: (" o   ",
                    "/|\\ ",
                    "/ \\")}

def display_man(guess_no):

        print("*****************")
        print("─┐───────────")

        for i in hangman_arts[guess_no]:
            print(i)

        print("******************")

def display_result(hint):
    
    print(" ".join(hint))
    print()

def display_answer(answer):

    print(" ".join(answer))
    

def main():

    guess_no = 0
    guesses = set()

    answer = random.choice(options)
    hint = ["_"] * len(answer)

    running = True
    while running:
        
        display_man(guess_no)
        display_result(hint)

        guess = input("Enter a letter : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess")
            continue
    
        if guess in guesses:
            print(f"{guess} is already guessed")
            continue
        
        guesses.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess       
        else:
            guess_no += 1

        if '_' not in hint:
            display_man(guess_no)
            display_answer(answer)
            print("You win!")
            running = False

        elif guess_no >= 6:
            display_man(guess_no)
            display_answer(answer)
            print("You lose!")
            running = False

if __name__ == '__main__':
    main()




