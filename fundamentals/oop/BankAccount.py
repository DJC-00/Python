class BankAccount:
    bankName = "DOJO Credit Union"
    allAccounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0, balance = 0):
        if int_rate > 1:
            self.intRate = int_rate/100
        elif int_rate < 1 and int_rate > 0:
            self.intRate = int_rate
        else:
            int_rate = 0;
        self.balance = balance
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

act1 = BankAccount(.4,22000)
act2 = BankAccount(37, 90000)

act1.displayAccountInfo()
act2.displayAccountInfo()

act1.deposit(500).deposit(440).deposit(230).withdrawl(244).yieldInterest().displayAccountInfo()
act2.deposit(500).deposit(440).withdrawl(244).withdrawl(5333).withdrawl(2244).withdrawl(9094).yieldInterest().displayAccountInfo()

BankAccount.showAllAccounts()
