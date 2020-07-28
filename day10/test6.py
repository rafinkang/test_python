'''
    마린 스팀팩()
    메딕 hp, x, y, mp, 방어력, 치료력
        heal(), move(), hold()

'''
import time
class Marine:
    def __init__(self):
        self.name = '마린'
        self.hp = 100
        self.attackPoint = 4
        self.attackSpeed = 1
        print('------------객체 초기화------------------------------')

    def attack(self, other):
        if other.hp > 4:
            other.hp -= self.attackPoint
            time.sleep(self.attackSpeed)
        else:
            print('고마해라 마이뭇따 아이가')
            return False

        print("체력이 %d 상태입니다."%other.hp)
        return True

    def move(self):
        pring("GoGoGo!")
    
    def upgrade(self):
        print("공격력 증가!")
        self.attackPoint += 7
    
    def steampack(self):
        print("스팀팩!!!!")
        self.hp -= 5
        self.attackSpeed = 0.5

class Medic:
    def __init__(self):
        self.hp = 100
        self.x = 10
        self.y = 10
        self.mp = 100
        self.amor = 10
        self.healSize = 10

    def heal(self, other):
        if other.hp < 100:
            other.hp += self.healSize
            if other.hp > 100: other.hp = 100
        else:
            return False
        print(other.name+"의 체력이 %d 만큼 회복되었습니다."%self.healSize)
        return True

m1 = Marine()
m2 = Marine()
m1.name = "마린1"
m2.name = "마린2"
m1.attack(m2)
m1.attack(m2)
m1.attack(m2)
m1.attack(m2)
m2.upgrade()
m1.steampack()
m2.attack(m1)
for i in range(100):
    if not m1.attack(m2):
        break

me = Medic()
while True:
    if not me.heal(m2): # 마린의 체력 10정도 증가
        break