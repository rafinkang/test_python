# 1. 클래스, 객체, 인스턴스? 

# 2.  아무것도 없는  Cat 클래스를 정의하세요 
class Cat:
    def __init__(self, name, age):
        print("야옹야옹")
        self.name = name
        self.age = age

    def __del__(self):
        print("고양이 죽는다 야옹")

    def __str__(self):
        return "이름 : "+str(self.name)+", 나이 :"+str(self.age)

    def eat(self, food):
        print(self.name,"가 ",food,"를 먹고있어요.")

    def info(self):
        print("이름 :", self.name, ", 나이 :", self.age)

    def play(self, what):
        print(what, "을 가지고 놀고 있다 냐옹")

# 3.  다음 코드로 야옹야옹 이라는 메세지를 출력하도록 Cat 클래스를 수정하세요 
#      nabi = Cat()
#      야옹야옹  
# nabi = Cat()
# 4. 
#       nabi.play("공")
#      공을 가지고 놀고 있다냐옹 
# nabi.play("공")
# 5.   생성자 추가 
#      nabi2 = Cat("나비", 2)
nabi2 = Cat("나비", 2)
# 6.
#     print(nabi2)
#     이름 : 나비 , 나이 : 2 
print(nabi2)
# 7. 
#      nabi2.info()
#     이름 : 나비 , 나이 : 2 
nabi2.info()
# 8.
#      nabi2.eat("생선")
#      나비가 생선을 먹고 있어요 
nabi2.eat("생선")
# 9.
#      del  nabi2 
#      고양이 죽는다 야옹 
del nabi2
# 10.  Customer 인스턴스를 생성할수 있도록 클래스를 정의하세요 
#       c =   Customer ("홍길동", 20, "990101-1234567")
class Customer:
    def __init__(self, name, age, birth):
        self.name = name
        self.age = age
        self.birth = birth
        self.balance = 0
        self.cnt = 0

    def __del__(self):
        print("그동안 이용해주셔서 감사합니다.")
        print("계좌 잔액 :", self.balance)

    def show(self):
        print(self.name,"님 현재 잔액은", self.balance,"원 입니다.")

    def deposit(self, money):
        self.balance += money
        self.cnt += 1
        print(self.name,"님 계좌에", money,"원 입금합니다.")
        if self.cnt % 5 == 0:
            print("이자발생!!")
            self.balance *= 1.05
        print(self.name,"님 현재 잔액은", self.balance,"원 입니다.")

    def withDraw(self, money):
        if self.balance > money:
            self.balance -= money
            print(self.name,"님 계좌에서", money,"원 출금합니다.")
        else:
            print("잔액이 부족합니다.")
        print(self.name,"님 현재 잔액은", self.balance,"원 입니다.")

    def get_balance(self):
        return "잔액값 가져오기: " + str(self.balance)

    def set_balance(self, money):
        self.balance = money
        print("잔액을 "+str(money)+"으로 변경")

c = Customer("홍길동", 20, "990101-1234567")
# 11. 
#       c.show()
#      # 홍길동님 현재 잔액은 0원입니다. 
c.show()
# 12. 
#        c.deposit(5000)
#      # 홍길동님 계좌에 5000원 입금합니다.
#      # 홍길동님 현재 잔액은 5000원입니다. 
c.deposit(5000)
# 13.
#        c.withDraw(9000)
#     # 잔액이 부족합니다. 
#      # 홍길동님 현재 잔액은 5000원입니다. 
c.withDraw(9000)
# 14.
#     c.withDraw(2000)
#     # 홍길동님 계좌에 2000원 출금합니다.
#      # 홍길동님 현재 잔액은 3000원입니다. 
c.withDraw(2000)
# 15.
#        Customer 클래스에 인스턴스 속성의 값을 을 수정할수 있는 setter, getter 
# 	클 추가합니다. 
#       print(c.get_balance()) # 잔액값 가져오기 : 3000
#       c.set_balance(30000) # 잔액을 30000으로 변경 
print(c.get_balance())
c.set_balance(30000)
# 16.
# 	5회 입금할때마다 
# 	잔액의 5%씩 이자 발생 
# 	c.deposit(1000)  #   31000
# 	c.deposit(3000)  #   34000
# 	c.deposit(2000)  #   36000
# 	c.deposit(2000)  #   38000
# 	c.deposit(3000)  #   41000
# 	# 이자발생   # 43050
c.deposit(1000)  #   31000
c.deposit(3000)  #   34000
c.deposit(2000)  #   36000
c.deposit(2000)  #   38000
c.deposit(3000)  #   41000

# 17.
# 	del c 
# 	# 그 동안 이용해주셔서 감사합니다 
# 	# 계좌 잔액 : 43050 

del c

