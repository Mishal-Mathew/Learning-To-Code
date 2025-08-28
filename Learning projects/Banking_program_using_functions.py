def S_balance(balance):
    return f"Your balance is ${balance:.2f}"

def deposit():
    amount = float(input("Enter the amount to deposit : "))
    if amount <= 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw : "))
    if amount < 0:
        print("Invalid amount")
        return 0
    elif balance - amount < 0:
         print("Insufficent funds")
         return 0
    else:
        return amount


def main():  
    balance = 0 
    running = True
    print("*******************")
    print("  Banking program  ")
    print("*******************")
    while running:
        print()
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*******************")
        choice =input("Enter your choice(1-4) : ")
        print("*******************")
        match choice:
            case '1':
                print(S_balance(balance))
            case '2':
                amount = deposit()
                balance += amount
                if amount != 0:
                    print(f"${amount:.2f} deposited successfully")
                else:
                    print("Transaction failed")
            case '3':
                amount = withdraw(balance)
                balance -= amount
                if amount != 0:
                    print(f"${amount:.2f} has been withdrawn from your account")
                else:
                    print("Transaction failed")
            case '4':
                print("Thank you for banking with us")
                running = False
            case _:
                print("Invalid choice")


if __name__ == '__main__':
    main()
   