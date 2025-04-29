class BankAccount:
    def __init__(self,name,accno,bal):
        self.name=name
        self.accno=accno
        self.balance=bal

    def deposit(self):
        amount=float(input('Enter amount to be deposited : '))
        if amount>0:
            self.balance+=amount
            print('\nAmount Deposited :',amount)
        else:
            print('Amount must be greater than 0')

    def withdraw(self):
        amount=float(input('Enter amount to be withdrawn : '))
        if self.balance-1000>=amount:
            self.balance-=amount
            print('\nYou withdrew : ',amount)
        else:
            print('Insufficient balance cannot withdraw')

    def getbalance(self):
        print('Your balance is: ',self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,name,accno,bal,rate):
        super().__init__(name,accno,bal)
        self.intrate=rate

    def acc_interest(self,months):
        interest=self.balance*self.intrate*months/(100*12)
        print('Interest {} added to balance' .format(interest))
        self.balance+=interest

name=input('Enter name of Account holder : ')
accno=int(input('Enter Account Number : '))
bal=float(input('Enter Opening Balance of Account : '))
rate=float(input('Enter Interest Rate : '))
s=SavingsAccount(name,accno,bal,rate)

while True:
    print('\nBank Menu')
    print('1.Deposit')
    print('2.Withdraw')
    print('3.Accumulate Interest')
    print('4.Display Balance')
    print('5.Exit')
    choice=int(input('Enter your choice :'))
    if choice==1:
        s.deposit()
    elif choice==2:
        s.withdraw()
    elif choice==3:
        months=int(input('For how many months : '))
        s.acc_interest(months)
    elif choice==4:
        s.getbalance()
    elif choice==5:
        break
    else:
        print('Invalid Choice')
