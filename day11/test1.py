class Test:
    def __init__(self, balance):
        self.balance = balance      # 인스턴스 변수

    def print(self):                # 인스턴스 함수
        print("잔액: ", self.balance)

t = Test(500)                       # 인스턴스 생성 -> 인스턴스 오브젝트들이 메모리에 올라감
t.aaa = 200

t.print()
print(t.aaa)
