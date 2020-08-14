class Account:
    # Construct an Account object

    def __init__(self, id, balance = 100, annualInterestRate = 0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        elif self.balance - amount < 0:
            print("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount


def getAChoice():
    while True:
        print("\nMain menu");
        print("1: check balance");
        print("2: withdraw");
        print("3: deposit");
        print("4: exit");
        print("Enter a choice: ", end = "");
        choice = eval(input())
        if choice < 1 or choice > 4:
            print("Wrong choice, try again: ", end = "")
        else:
            break

    return choice

# Create 10 accounts


def main():
    print("HELLO")
    accounts = []
    for i in range(10):
        accounts.append(Account(i, 100))

    while True:
        id = eval(input("Enter an account id: "))
        if id < 0 or id > 10:
            print("Please enter a correct id")
            continue;

        while True:
            choice = getAChoice()

            if choice == 1:
                print("The balance is", format(accounts[id].getBalance(), ".2f"))
            elif choice == 2:
                if accounts[id].getBalance() == 0:
                    print("Insufficient funds")
                else:
                    amount = eval(input("Enter an amount to withdraw: "))
                    accounts[id].withdraw(amount)
            elif choice == 3:
                amount = eval(input("Enter an amount to deposit: "))
                accounts[id].deposit(amount)
            elif choice == 4:
                break


main()


'''
Enter an account id: 0

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 1
The balance is 100.00

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 2
Enter an amount to withdraw: 200
Insufficient funds

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 2
Enter an amount to withdraw: 100

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 2
Insufficient funds

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 4
Enter an account id: 1

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 3
Enter an amount to deposit: 50

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 1
The balance is 150.00

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 4
Enter an account id: 0

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 1
The balance is 0.00

Main menu
1: check balance
2: withdraw
3: deposit
4: exit
Enter a choice: 4
'''