class Person:
    '''
    인간 클래스
    '''
    def __init__(self):
        print(id(self))
        print('Person Class 초기화 함수')
        self.name = "홍길동"
        self.age = 20
        self.job = "도적"
        self.eat_cnt = 0

    def eating(self, what):
        self.eat_cnt += 1
        print(what, "을/를 맛있게 먹어요", self.eat_cnt)
    

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