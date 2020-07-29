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
    
if __name__ == "__main__":
    p1 = Person()
    print(p1.name)
    print(p1.age, p1.job)
    p1.eating("바아아압")

    print('---------------------------------------')
    p2 = Person()
    p2.name = "구구구"
    print(p2.name)

    print('---------------------------------------')
    print("id(p1): ", id(p1), "// id(p2): ", id(p2))