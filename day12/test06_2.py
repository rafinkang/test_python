
# Player
# hp 
# name 

# Player has a Gun 

class Weapon:
    def __init__(self):
        pass
    def use(self):
        pass
    def reuse(self):
        pass


class Grenade:
    pass

class Bomb:
    pass


class Sword(Weapon):
    def __init__(self,name):
        self.name = name
    def use (self):
        self.swing()

    def swing(self):
        print(self.name , "을 휘두릅니다.")
    


class Gun(Weapon):
    def __init__(self,  name, bullet):
        self.bullet = bullet
        self.name = name
    def use(self):
        self.fire()

    def fire(self):
        if self.bullet >= 1:
            print("빵야~~~~~ ")
            self.bullet -= 1 
        else:
            print("틱~")
    def reload(self):
        print("찰카닥")
        self.bullet=20



class Player:
    def __init__(self, name):
        self.hp = 100
        self.name = name
        self.weapon = None

    def receive(self, weapon):
        self.weapon =weapon
        
    def use(self):
        self.weapon.use()
       

p = Player("홍기동")
s = Sword("엑스칼리버")
g = Gun("AK47",20)
p.receive(g)

#p.receive(g)
p.use()



# 수류탄
# 데미지 

# 칼

# 폭탄 

# 총


