class User:
    def __init__(self,name,email,initBalance = 0):
        self.name = name
        self.email = email
        self.balance = initBalance

    def accountInfo(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nAccount Balance: ${self.balance}\n")

    def displayBalance(self):
        print(f"Your balance is: ${ self.balance}\n")

    def makeWithdrawl(self, amount):
        if (self.balance >= amount):
            self.balance-= amount;
            print(f"Welcome: {self.name}\nYou have made a withdrawl of ${amount}")
        else:
            print("Account Balance Too Low\n")
        self.displayBalance()

    def makeDeposit(self, amount):
        self.balance += amount;
        print(f"Welcome: {self.name}\nYou have made a deposit of ${amount}")
        self.displayBalance();

    def moneyTransfer(self, user, amount):
        if self.name == user.name:
            print(f"{self.name}, You cannot transfer money to yourself.")
        else:
            self.balance -= amount;
            user.balance += amount;
            print(f"Okay {self.name}, transfering ${amount} to {user.name}")


Bob = User('Bob','bobob@gmail.com',10000)
Tim = User('Tim','TimmyT@msn.com',40500)
Noah = User('Noah','No_Uh123@aol.com',56610)

Bob.accountInfo()
Tim.accountInfo()
Noah.accountInfo()

Bob.makeWithdrawl(100)
Bob.makeWithdrawl(200)
Bob.makeWithdrawl(300)
Bob.makeDeposit(600)
Bob.accountInfo()

Tim.makeWithdrawl(300)
Tim.makeWithdrawl(300)
Tim.makeDeposit(600)
Tim.makeDeposit(600)
Tim.accountInfo()

Noah.makeDeposit(600)
Noah.makeWithdrawl(300)
Noah.makeWithdrawl(300)
Noah.makeWithdrawl(300)
Noah.accountInfo()

Bob.moneyTransfer(Noah, 200)