import random
import time
#7️⃣💰🍇

def get_symbol():

    symbols = ('7️⃣ ','💰','🍇')

    selected = []
    selected = [random.choice(symbols) for _ in range(3)]
    print("Spinning....\n")

    time.sleep(1)

    print("******************")

    return selected

def checking(selected,bet):

    if selected[0]==selected[1]==selected[2]:
        if selected[0]=='7️⃣':

            return bet*10

        if selected[0]=='💰':

            return bet*5 

        if selected[0]=='🍇':

            return bet*3
    else:

        print("******************")
        print("\nSorry!You lost.Better luck next time!")

        return 0

def main():

    print("*****************")
    print("Slot Machine")
    print("Symbols:  7️⃣  💰 🍇")
    print("*****************")

    balance = 100

    user_ask = "Y"

    print(f"\nCurrent balance : ${balance:.2f}")

    while user_ask == "Y":

        bet = input("Place your bet amount : ")

        if not bet.isdigit():
            print("\nInvalid amount")

        else:

            bet = int(bet)
            
            if bet > balance:
                print("\nInsufficent funds")
                continue

            elif bet <= 0:
                print("Bet must be greater than zero")
                continue

            else:

                balance -= bet
                selected = get_symbol()

                print("  |  ".join(selected))

                amount = checking(selected,bet)
                balance += amount

                if amount > 0:
                    print(f"You have won ${amount:.2f}")

                print(f"Your balance is ${balance:.2f} ")

        if balance == 0:

            print("Insufficent funds")
            break

        user_ask = input("Do you want to play again?(Y/N): ").upper()

        if user_ask != "Y":
            
            print("Thanks for playing.See you next time!")

if __name__ == '__main__':
    main()