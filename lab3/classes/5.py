#Create a bank account class that has attributes owner, 
#balance and two methods deposit and withdraw. 
#Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner = "", balance = 0):
        self.balance = balance
        self.owner = owner

    def deposit(self):
        dengidengi = int(input("Deposite sum: "))
        self.balance += dengidengi
        print("Succesfully!")
        print(f"Your current balance(tg): {self.balance}")
    
    def withdraww(self):
        withdraw = int(input("Output sum: "))
        if withdraw > self.balance:
            print("Not enough cash!")
        else:
            self.balance -= withdraw
            print("Succesfully!")
            print(f"Your current balance(tg): {self.balance}")

bankOperation = Account(input("Fido:"), int(input("Enter your balance: ")))
while True:
    typeoper = input("Enter operation type (Withdraw/Deposit/Exit): ")
    if typeoper == "Withdraw":
        bankOperation.withdraww()
    elif typeoper == "Deposit":
        bankOperation.deposit()
    elif typeoper == "Exit":
        break
    else:
        print("Incorrect entry of operarions.")