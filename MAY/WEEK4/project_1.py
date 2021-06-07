"""
Create a python class ATM which has a parametrised constructor (card_no, acc_balance).
Create methods withdraw(amount) which should check if the amount is available on the
account if yes, then deduct the amount and print the message “Amount withdrawn”, if the
amount is not available then print the message “OOPS! Unable to withdraw amount, Low
balance”. Create another method called, deposit, which should deposit amount if amount is
positive and should print message “Amount deposited”. If not, print message “Invalid amount
to deposit”. Create a method called getBalance which should print current balances at any
given point of time.
Example: atm_acc_1 = ATM(“1234”, 400)
	 	 	 atm_acc_2 = ATM(“10001”, 100)
Test cases:

atm_acc_1.withdraw(300)     Amount withdrawn     
atm_acc_1.withdraw(300)     OOPS! Unable to withdraw amount, Low balance
atm_acc_1.deposit(300)      Amount Deposited
atm_acc_1.getBalance()      400
atm_acc_2.getBalance()      100 
atm_acc_2.deposit(300)      Amount Deposited 
atm_acc_2.getBalance()      400
"""
class ATM:
    def __init__(self,card_no,acc_balance):
        self.card_no = card_no
        self.acc_balance= acc_balance

    def withdraw(self,amount):
        if(amount<= self.acc_balance ):
            self.acc_balance = self.acc_balance-amount
            return "Amount withdrawn"
        else:
            return "OOPS! Unable to withdraw amount, Low balance"
    def deposit(self,amount):
        if(amount>0):
            self.acc_balance = self.acc_balance+amount
            return "Amount Depositted"
        else:
            return "Invalid amount to deposit"
    def getBalance(self):
        return self.acc_balance

atm_acc_1 = ATM("1234",400)
atm_acc_2 = ATM("10001",100)

print(atm_acc_1.withdraw(300))
print(atm_acc_1.withdraw(300))
print(atm_acc_1.deposit(300))
print(atm_acc_1.getBalance())
print(atm_acc_2.getBalance())
print(atm_acc_2.deposit(300))
print(atm_acc_2.getBalance())
