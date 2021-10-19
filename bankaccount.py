# bankaccount.py

class BankAccount:
    def __init__(self, id, name, balance):
        #이름숨김 : 복잡한 이름으로 변경
        self.__id = id
        self.__name = name
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount 
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, self.__name, self.__balance)

account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
#print(account1)
print(account1._BankAccount__balance)
