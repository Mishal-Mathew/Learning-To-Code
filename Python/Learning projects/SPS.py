import random
import time
print("********************************************************************")
print("        Welcome to the game of Stone , Scissor and Paper            ")
print("********************************************************************")
time.sleep(1)
def retry():
    rounds = input("Enter the no of rounds you want to play: ")
    while rounds.isdigit() == False or int(rounds) < 1:
        print("Invalid input")
        rounds = input("Enter the no of rounds: ")

    rounds = int(rounds)
    game(rounds)
def game(rounds):
    while rounds != 0:

        def data_entry():
            choices = ("Stone" , "Scissor" , "Paper")
            comp = random.choice(choices)
            
            user = ""
            user = input("\nEnter a choice: ").capitalize()
            print()
            while user not in choices:
                    print("Invalid input\n")
                    user = input("Enter a choice: ").capitalize()
            checking(comp,user)

        def checking(comp , user):
            
            print(f"\nComputer : {comp} \nUser      : {user}")
            if comp == "Stone" and user == "Paper" or comp == "Scissor" and user == "Stone" or comp == "Paper" and user == "Scissor":
                print("\nYou Won!")
            elif comp == user:
                print("\nIt's a Draw!")
            else:
                print("\nYou lost!")

        def main():
            data_entry()

        if __name__ == '__main__':
            main()

        rounds -= 1
    re = input("\nWould you like to play again?: ").upper()
    if re == "YES":
        retry()
    else:
        print("Thanks for playing!")
retry()
