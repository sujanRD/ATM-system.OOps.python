from abc import ABC ,abstractmethod
class ATM(ABC):
    @abstractmethod
    def deposit(self,amount):
        self.amount=amount
        pass
    @abstractmethod    
    def withdraw(self,amount):
        self.amount=amount
        pass
    @abstractmethod    
    def check_balance(self):
        pass
    @abstractmethod
    def change_pin(self):
        pass
class Bank_account(ATM):
    def __init__(self,holder_name,balance,pin):
        super().__init__()
        self.holder_name=holder_name
        self.__balance=balance
        self.__pin=pin
    def deposit(self,amount):

        if amount > 0:
            self.__balance+= amount
            print("After depositing=",self.__balance)
        else:
            print("enter  positive amount")
    def withdraw(self, amount,PIN):
        if PIN == self.__pin :
            if amount > self.__balance:
                print("Low balance")
            else:
                self.__balance-=amount
                print("After withdrawing=",self.__balance)
        else:
            print("Wrong PIN, Try again!!")
    def check_balance(self,PIN):
        if PIN == self.__pin:
            print("Total balance =",self.__balance)
        else:
            print("Wrong PIN, Try again!!")
    def change_pin(self,PIN,new_pin):
        if PIN ==self.__pin:
            PIN=new_pin
            print("PIN changed sucessfuly")
        else:
            print("Wrong PIN, Try again!!")

B=Bank_account('sujan',5000,2345)
while True:
    print("         ------ATM------    ")
    print("          1.Deposit")
    print("          2.withdraw")
    print("          3.check balance")
    print("          4.change pin")
    print("          5.Exit")
    choice=int(input("        enter choice(1-5) :"))
    if choice ==1:
        amount=int(input("     enter amount to deposit:"))
        B.deposit(amount)
    elif choice==2:
        amount=int(input("      enter amount to withdraw:"))
        PIN=int(input("        enter correct pin:"))
        B.withdraw(amount,PIN)
    elif choice==3:
        PIN=int(input("      enter correct pin:"))
        B.check_balance(PIN)
    elif choice==4:
        PIN=int(input("     enter correct pin:"))
        new_pin=int(input("     enter new pin:"))
        B.change_pin(PIN,new_pin)
    elif choice==5:
        print("    ------Thanks------")
        break
    else:
        print("  may be details wrong,TRy again!!")


        






    
        


         
