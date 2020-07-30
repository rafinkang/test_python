# 붕붕 클래스
class Car:
    def __init__(self, 
                handle = 1, 
                wheel = 4, 
                eye = 2, 
                nose = 1, 
                mouse = 1 ):
        print("----car class 초기화 ---------------")
        self.handle = handle
        self.wheel = wheel
        self.eye = eye
        self.nose = nose
        self.mouse = mouse
    
    def __add__(self, other_car):
        print("충돌났어요 ㅠㅠ")

    def __sub__(self, other_car):
        print("빼부럿으~빼부러쓰~")

    def run(self):
        print(self.wheel, "붕붕카 달리는중")
    
    def stop(self):
        print("정지~")

    def smell(self, what):
        print(what, "냄새 맡는중")

    def talk(self):
        print("수다떠는중")

# 오픈카 클래스
class InheritedCar(Car):
    def __init__(self, handle=1, wheel=4, eye=2, nose=1, mouse=1):
        super().__init__(handle=handle, wheel=wheel, eye=eye, nose=nose, mouse=mouse)
        print("----InheritedCar class 초기화 ---------------")


    def light_on(self):
        print("라이트를 켜요")

    def run(self):
        print("오픈카로 달려요")


c1 = Car()
# c1.talk()
# print(c1.handle)
ic1 = InheritedCar()
c1.smell("꽃")      # 꽃 냄새 맡는중
c1.run()            # 4 붕붕카 달리는중
ic1.smell("장미")   # 장미 냄새 맡는중
ic1.light_on()      # 라이트를 켜요
ic1.run()           # 오픈카로 달려요

# c1 + ic1 연산 불가능하다.
# but __add__() 매직메서드를 작성하게 되면 오버로딩으로 동작한다.
c1 + ic1 

c1 - ic1