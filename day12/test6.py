# 서든어택

# Player - hp, name

# 수류탄
# 칼
# 폭탄설치
# 총 - 데미지 장탄수 등

class Gun:
    def __init__(self, name, damage, bullet):
        self.name = name
        self.damage = damage
        self.bullet = bullet
    def fire(self):
        print(self.name, "빵야빵야")

class Knife:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def fire(self):
        print(self.name, "휘적휘적")

class Grenade:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def fire(self):
        print(self.name, "파이어인더홀")

class C4:
    def __init__(self, name):
        self.name = name
    def fire(self):
        print(self.name, "뱅~~~~")

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = Gun("AK", 30, 20)
        self.knife = Knife("식칼", 5)
        self.grenade = Grenade("눈뽕", 1)
        self.c4 = C4("씨포")

    def fire_gun(self):
        self.gun.fire()
    def fire_knife(self):
        self.knife.fire()
    def fire_grenade(self):
        self.grenade.fire()
    def fire_c4(self):
        self.c4.fire()

p = Player("서든초보")
p.fire_gun()