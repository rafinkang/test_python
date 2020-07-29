from test9 import Animal

class Monkey(Animal):
    def __init__(self):
        print("원숭이 초기화 함수-------------------")
        self.eyes = 2
        self.mouth = 1
        self.ears = 2 
        self.species = "긴팔"
        self.name = "숭구리당당숭당당"

    # def jump(self):
    #     print("폴짝폴짝 뛰어요")

    # def eating(self):
    #     print("바나나를 먹어요")

    # def sleeping(self):
    #     print("매달려서 쿨쿨 자요 부럽게ㅡㅡ")

if __name__ == "__main__":
    m = Monkey()
    m.jump()
    m.eating()
    m.sleeping()