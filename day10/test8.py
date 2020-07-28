# 객체 지향 구구단
# 3 * 1 = 3
# ...
# 3 * 9 = 27
class GuGuDan:
    def __init__(self):
        self.dan = 1

    def print(self):
        print("=====", self.dan,"단 =====")
        for j in range(1, 10):
            print(self.dan, '*', j, '=', self.dan*j)


g = GuGuDan()
g.dan = 3
g.print()
g.dan = 7
g.print()
g.dan = 9
g.print()