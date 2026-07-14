class Account:
    def __init__(self,name,balnce):
        self.name=name
        self.__balance=balnce
        if self.__class__.__name__ == "Current_Account":
            self.__overdraft= 20000 + (self.__balance*0.2)
        else:
            pass
    
    def Withdraw(self,Amount):
        if Amount <= self.__balance and Amount > 0:
            self.__balance -= Amount
            print("Amount Succesfully Withdraw")
        elif Amount <= self.__overdraft + self.__balance and Amount > 0:
            print("Ammount Succesfully Withdrawa")
            self.__balance -= Amount
        else:
            print("Insufficent Amount or INcorrect Amount")

    
    def Deposit(self,Amount):
        if 0 < Amount:
            self.__balance += Amount
            print("Amount Succesfully Deposited....")
        else:
            print("Deposit a Valid Amount")
            print("Try Again")
            
    
    def Get_Balance(self):
        return self.__balance

class Saving_Account(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)


class Current_Account(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance) 



Acc1=Saving_Account("Krushna",10000)
Acc2=Current_Account("Mane",50000)
Acc1.Withdraw(5000)
print(Acc1.Get_Balance())

Acc2.Withdraw(100000)
print(Acc2.Get_Balance())
