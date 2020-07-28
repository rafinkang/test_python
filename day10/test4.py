class Human:
    def __init__(self, name, age, job):
        print("초기화 함수호출 - 생성자")
        self.name = name
        self.age = age
        self.job = job

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
        print('----------------------------')
        print('이름 :', self.name)
        print('나이 :', self.age)
        print('직업 :', self.job)
        print('눈 :', self.eye)
        print('입 :', self.mouth)
        print('귀 :', self.ear)
        print('----------------------------')

p1 = Human('펭수',10,'EBS직원')
p1.status()

p2 = Human('고길동', 30,'재벌2세')
p2.status()

p3 = Human('둘리',10000000,'백수')
p3.status()