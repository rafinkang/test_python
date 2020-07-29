from test9 import Animal
import os
print(os.getcwd())
class Whale(Animal):
    def __init__(self):
        print("고래 초기화 함수-----------------")
        self.eyes = 2
        self.mouth = 1
        self.species = "돌"
        self.name = "고래까와"

    # def jump(self):
    #     print("첨벙첨벙 뛰어요")
    
    # def eating(self):
    #     print("새우잡아 먹어요")

    # def sleeping(self):
    #     print("물속에서 자나봐요")

if __name__ == "__main__":
    w = Whale()
    print(w.name)
    w.jump()
    w.eating()
    w.sleeping()