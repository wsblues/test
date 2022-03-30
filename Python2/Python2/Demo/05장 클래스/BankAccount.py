# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 인스턴스
    def __init__(self, id, name, balance, temp=0):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
        self.temp = temp
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
        # print(id(self.__id))
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

a = 100
b = '전우치'
c = 15000
print(id(a))
a = 1000
print(id(a))
account1 = BankAccount(a,b,c)
account1.withdraw(3000)
# account1.__balance = 100
#_클래스__맴버변수 : 접근 가능
# print(account1.__balance)
print(account1._BankAccount__balance)
account1.temp = 10
print(account1.temp)

# print(account1.__balance)