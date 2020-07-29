from test9 import Animal
class Rabbit(Animal):
    def __init__(self, foots):
        super().__init__(foots)  # 부모객체의 init을 불러온다
        print("토끼 초기화 함수--------")
        # self.eyes = 2
        # self.mouth = 1
        # self.ears = 2
        self.species = "앙골라"
        self.name = "토순이"

    # def jump(self):
    #     print("깡총깡총 뛰어요")

    # def eating(self):
    #     print("당근을 먹어요")

    # def sleeping(self):
    #     print("쿨쿨 자요 부럽게ㅡㅡ")

if __name__ == "__main__":
    r = Rabbit(4)
    print(r.eyes)
    r.jump()
    r.eating()
    r.sleeping()


# test5 -> 워ㄴ숭이
# test6 -> 고래 구현 ㄱ