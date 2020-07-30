
# Player
# hp 
# name 

# Player has a Gun 

class Grenade:
    pass

class Sword:
    def __init__(self,name):
        self.name = name

    def swing(self):
        print(self.name , "을 휘두릅니다.")
    

class Bomb:
    pass

class Gun:
    def __init__(self,  name, bullet):
        self.bullet = bullet
        self.name = name
    
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
        self.gun = None
        self.sword = None
    def receive_gun(self, gun):
        self.gun = gun
    def receive_sword(self, sword):
        self.sword = sword

    def use(self):
        if self.gun != None:
            self.gun.fire()
        elif self.sword != None:
            self.sword.swing()

p = Player("홍기동")
s = Sword("엑스칼리버")
g = Gun("AK47",20)
p.receive_sword(s)

#p.receive(g)
p.use()



# 수류탄
# 데미지 

# 칼

# 폭탄 

# 총


