class Human:
    def __init__(self):
        print("초기화 함수호출 - 생성자")
        self.name = "고길동"
        self.age = 30
        self.job = "고위공직자"
        self.eye = 2
        self.mouth = 1
        self.ear = 2

    def eating(self):
        print("냠냠 먹어 냠")

    def walking(self):
        print("뚜벅뚜벅")
    
    def sleeping(self):
        print("쿨쿨zZ")

    def thinking(self):
        print("생각한다 고로 존재한다.")
    
    def status(self):
        print('이름 :', self.name)
        print('나이 :', self.age)
        print('직업 :', self.job)
        print('눈 :', self.eye)
        print('입 :', self.mouth)
        print('귀 :', self.ear)

print(Human, id(Human), type(Human))

ko = Human()    # 인스턴스 변수 = 클래스명() # 클래스의 초기화함수(생성자)가 호출이 된다.
print(ko.name)  # . 연산자 의미 : 주소를 찾아가~
print(ko.age)
print(ko.ear)
print(ko.eye)
print(ko.job)
print(ko.mouth)

# 함수도 호출
ko.eating()
ko.walking()
ko.sleeping()
ko.thinking()

print('----------------------------------------------')

# 펭수
p = Human()
p.name = '펭수'
p.age = 10
p.job = "EBS 직원"

p.status()