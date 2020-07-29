class Player:

    # 클래스 속성
    cnt = 0
    bag = []

    def __init__(self, name):
        print("--------초기화 함수",name,"- 생성자--------")
        self.name = name
        Player.cnt += 1

    def put(self, obj):
        Player.bag.append(obj)

    def attack(self, other):
        print(other.name + "를 공격합니다.")

    def greeting(self, other):
        print(other.name + " 부모님은 잘 계시니?")

    # class method - 함수 위에 데코레이션으로 선언
    @classmethod
    def getBag(cls):
        print("인벤토리: ", cls.bag)

    
p1 = Player("에코")
print(p1.cnt)
p1.put("권총")

print('----------------------------')

p2 = Player("야스오")
print(p2.cnt)

print('----------------------------')

p1.greeting(p2)
p1.attack(p2)
# 클래스 속성(클래스변수)는 인스턴스끼리 공유한다.

print('----------------------------')

p1.getBag()
p2.getBag()