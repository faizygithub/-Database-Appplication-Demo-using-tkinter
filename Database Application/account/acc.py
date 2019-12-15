class Account:

    def __init__(self,filepath):
        self.filepath=filepath
        with open (filepath,'r') as file:
            self.balance=int(file.read())
    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))
class Checking(Account):
    """ This class generates Checking accounts"""
    type="checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee


jacks_checking=Checking("account\\jack.txt",1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

jhons_checking=Checking("account\\jhon.txt",1)
jhons_checking.transfer(100)
print(jhons_checking.balance)
jhons_checking.commit()
print(jhons_checking.type)
print(jhons_checking.__doc__)
#checking.deposit(10)


#account=Account("account//balance.txt")
#print(account.balance)SS
#print(account.balance)
#print(account.balance)
