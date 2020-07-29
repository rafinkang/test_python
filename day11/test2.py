# day10/test7.py
class ATM:
    def __init__(self):
        print('----------초기화 함수----------')
        self.name = "홍길동"
        self.__balance = 0       # _변수명 - 내부에서만 쓸거야 하는 변수 : 그냥 그렇다고 표현만
                                 # __변수명 - private 변수 : 강제

    # getter, setter
    def get__balance(self):
        # 감사기록
        # return self.__balance
        print("잔액 : ", self.__balance)

    def set__balance(self, balance):
        self.__balance = balance


    def deposit(self, money):
        self.__balance += money
        print("%s 원 입금이 완료되었습니다. \n 현재 잔액은 %s 원 입니다."%(format(money,','), format(self.__balance, ',')))
    
    def withDraw(self, money):
        if self.__balance - money > 0:
            self.__balance -= money
            print("%s 원 출금이 완료되었습니다."%(format(money,',')))
        else:
            print('잔액이 부족합니다.')

        print('현재 잔액은 %s원 입니다.'%(format(self.__balance, ',')))

    



auto = ATM()

# print(auto)
auto.deposit(100)
auto.aaa =300
# auto.set__balance(9999999)
auto.get__balance()
auto._ATM__balance = 77777
auto.get__balance()
print(auto._ATM__balance)
auto.withDraw(1000000)
print(auto._ATM__balance)
print("--------------------------")

auto.get__balance()