class Animal:
    def __init__(self, foots):
        print('animal 초기화 --------------')
        self.eyes = 2
        self.mouth = 1
        self.ears = 2
        self.foots = foots
    
    def jump(self):
        print("Animal 점핑!점핑!")

    def eating(self):
        print("Animal 먹는다 배고프다")
    
    def sleeping(self):
        print("Animal 잔다 졸리다 ㅠ")


