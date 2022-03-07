class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
        self.accounts.append(BankAccount())

    def accountInfo(self):
        print(f"Name: {self.name}\nEmail: {self.email}\n")
        for i in range(len(self.accounts)):
            print(f"Account Number: {i+1}\nAccount Balance: ${self.accounts[i].balance}\nInterest Rate: {(self.accounts[i].intRate * 100)}%\n")

    def displayBalance(self, acc = 0):
        if (self.hasMultipleAccounts() and self.inRange(acc)):
            print(f"Account Number: {acc+1}\nYour balance is: ${self.accounts[acc].balance}\n")

    def makeWithdrawl(self, amount, acc = 0):
        if (self.accounts[acc].balance >= amount):
            self.accounts[acc].balance -= amount;
            print(f"Welcome: {self.name}\nYou have made a withdrawl of ${amount} from Account Number: {acc+1}\n")
        else:
            print("Account Balance Too Low\n")
        self.displayBalance(acc = acc)

    def makeDeposit(self, amount, acc = 0):
        self.accounts[acc].balance += amount;
        print(f"Welcome: {self.name}\nYou have made a deposit of ${amount} to Account Number: {acc+1}\n")
        self.displayBalance(acc = acc);

    def moneyTransfer(self, user, amount, acc1 = 0, acc2 = 0):
        if self.name == user.name:
            print(f"{self.name}, You cannot transfer money to yourself.")
        else:
            if (self.accounts[acc1].balance - amount > 0):
                self.accounts[acc1].balance -= amount;
                user.accounts[acc2].balance += amount;
                print(f"Okay {self.name}, transfering ${amount} to {user.name}")

    def addAccount(self):
        self.accounts.append(BankAccount(accountNum=len(self.accounts)))

    def hasMultipleAccounts(self):
        if len(self.accounts) > 1:
            return True;
        else:
            print("Account Does Not Exist")
            return False;
    
    def inRange(self, accNum):
        if accNum >= 0 and accNum <= len(self.accounts)-1:
            return True;
        else:
            print("Account Does Not Exist")
            return False

class BankAccount:
    bankName = "DOJO Credit Union"
    allAccounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.02, balance = 0, accountNum = 0):
        if int_rate > 1:
            self.intRate = int_rate/100
        elif int_rate < 1 and int_rate > 0:
            self.intRate = int_rate
        else:
            int_rate = 0;
        self.balance = balance
        self.accountNum = accountNum
        BankAccount.allAccounts.append(self)
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount;
        return self;

    def withdrawl(self, amount):
        if (self.balance >= amount):
            self.balance-= amount;
        else:
            print("Account Balance Too Low\n")
        return self;
        
    def displayAccountInfo(self):
        print(f"Balance: ${self.balance}\nInterest Rate: {self.intRate}")
        return self;

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intRate)
        return self

    @classmethod
    def showAllAccounts(cls):
        for i in range(len(cls.allAccounts)):
            print(cls.allAccounts[i])

test = User("testName", "testEmail")
test2 = User("difName", "difEmail")
test.accountInfo()
test.addAccount()
test.makeDeposit(200)
test.accountInfo()
print(test.accounts[0].balance)
print(test.accounts[1].balance)
test.makeDeposit(200, 0)
test.makeDeposit(2100, 1)
test.accountInfo()
test2.accountInfo()
test.moneyTransfer(test2,200,1,0)
test.accountInfo()
test2.accountInfo()