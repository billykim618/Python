class Account:
    def __init__(self, id=0, number=100.0, annualInterestRate=0.0):
        self.__id = id
        self.__balance = number
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12

    def getMonthlyInterest(self):
        return self.getMonthlyInterestRate() * self.__balance / 100

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount


def main():
    account1 = Account(1122, 20_000, 4.5)

    print("Account's ID:", account1.getId())
    print("Account's current balance:", account1.getBalance())
    print("Account's annual interest rate:", account1.getAnnualInterestRate(), end="%\n")
    print("Account's monthly interest rate:", account1.getMonthlyInterestRate(), end="%\n")
    print("Account's monthly interest: $" + str(account1.getMonthlyInterest()))
    account1.withdraw(2500)
    print("Withdrew $2500")
    print("Account's new balance after withdrawal: $" + str(account1.getBalance()))
    account1.deposit(3000)
    print("Deposited $3000")
    print("Account's new balance after deposit: $", end="")
    print(account1.getBalance())
    print("Account's annual interest rate:", account1.getAnnualInterestRate(), end="%\n")
    print("Account's monthly interest rate:", account1.getMonthlyInterestRate(), end="%\n")
    print("Account's monthly interest: $" + str(account1.getMonthlyInterest()))


main()  # Invoke main method

'''
Account's ID: 1122
Account's current balance: 20000
Account's annual interest rate: 4.5%
Account's monthly interest rate: 0.375%
Account's monthly interest: $75.0
Withdrew $2500
Account's new balance after withdrawal: $20000
Deposited $3000
Account's new balance after deposit: $20000

Process finished with exit code 0
'''
