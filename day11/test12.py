import random
import math
class Agar:
    def __init__(self, color, nickname):
        self.radius = 5
        self.color = color
        self.nickname = nickname
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.weight = 10

    def feeding(self, other):
        if other.weight < self.weight:
            self.weight += other.weight
        else:
            self.weight += 17
            print("먹이주기")

    def split(self):
        self.weight = self.weight//2
        print("반쪼가리")

    def move(self):
        print("이동하기")

    def merge(self):
        self.weight += 1
        self.radius += 0.2
        print(" 셀 먹기")

    # @ㅇㅇㅇㅇ : 데코레이터
    # @staticmethod
    # def getArea(self, radius):
    #     return math.pi*radius**2
    
    @staticmethod
    def getArea(radius):
        return math.pi*radius**2

print(Agar.getArea(50))

# a1 = Agar("green", "파국이다")
# a1.move()
# print(a1.getArea())
# a1.merge()
# a1.merge()
# a1.merge()
# a1.merge()
# a1.merge()
# a1.merge()
# a1.merge()
# a1.split()
# print(a1.getArea())
