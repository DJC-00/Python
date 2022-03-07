class User:
    def __init__(self,name,email,initBalance = 0):
        self.name = name
        self.email = email
        self.balance = initBalance

    def accountInfo(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nAccount Balance: ${self.balance}\n")
        return self;

    def displayBalance(self):
        print(f"Your balance is: ${ self.balance}\n")
        return self;

    def makeWithdrawl(self, amount):
        if (self.balance >= amount):
            self.balance-= amount;
            print(f"Welcome: {self.name}\nYou have made a withdrawl of ${amount}")
        else:
            print("Account Balance Too Low\n")
        self.displayBalance()
        return self;

    def makeDeposit(self, amount):
        self.balance += amount;
        print(f"Welcome: {self.name}\nYou have made a deposit of ${amount}")
        self.displayBalance();
        return self;

    def moneyTransfer(self, user, amount):
        if self.name == user.name:
            print(f"{self.name}, You cannot transfer money to yourself.")
        else:
            self.balance -= amount;
            user.balance += amount;
            print(f"Okay {self.name}, transfering ${amount} to {user.name}")
        return self;

Bob = User('Bob','bobob@gmail.com',10000)
Tim = User('Tim','TimmyT@msn.com',40500)
Noah = User('Noah','No_Uh123@aol.com',56610)

Bob.accountInfo()
Tim.accountInfo()
Noah.accountInfo()

Bob.makeWithdrawl(100).makeWithdrawl(200).makeWithdrawl(300).makeDeposit(600).accountInfo()

Tim.makeWithdrawl(300).makeWithdrawl(300).makeDeposit(600).makeDeposit(600).accountInfo()

Noah.makeDeposit(600).makeWithdrawl(300).makeWithdrawl(300).makeWithdrawl(300).accountInfo()

Bob.moneyTransfer(Noah, 200)