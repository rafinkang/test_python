# 상속 : class 클래스명(부모클래스명)
class Person:
    # 인간 클래스
    def __init__(self):
        print('Person Class 초기화 함수')
        self.name = "홍길동"
        self.age = 20
        self.job = "도적"

    def eating(self, what):
        print(self.name, "이", what, "을/를 맛있게 먹어요")

    def sleeping(self):
        print("이새끼 또자요")

# person 클래스를 상속받은 슈퍼맨클래스
class SuperMan(Person):
    def __init__(self, name, age, job, hobby):
        print('슈퍼맨 초기화 함수')
        self.name = name
        self.age = age
        self.job = job
        self.hobby = hobby

    def fly(self):
        print("비행 : 날아보아요~~~")
        print("??????")

    def laser(self):
        print('찌이이이ㅣ이이이ㅣ ㅇ .ㅇ-----')



if __name__ == "__main__":
    sm = SuperMan("슈퍼맨", 20, "신문기자", "연애")
    sm.fly()
    sm.laser()
    sm.eating("밥")
    sm.sleeping()
