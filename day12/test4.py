# Gun 클래스

class Gun:
    def __init__(self, name, bullet):
        self.bullet = bullet
        self.name = name

    def fire(self):
        if self.bullet >= 1:
            print("빵야~~")
            self.bullet -= 1
        else:
            print("틱~")
    
    def reload(self):
        self.bullet = 20
        print("찰카닥")

# g = Gun("AK47", 20)

# for i in range(30):
#     g.fire()

# g.reload()
# g.fire()

class Police():
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age
        self.gun = None
        
    def receive_gun(self, gun):
        self.gun = gun

    def patrol(self):
        print("순찰중....")

    def arrest(self, who):
        print(who, "을 체포합니다.")
    
    def notify_mranda_rights(self):
        print("당신은 묵비권을 행사할..........")

    def eat_donut(self):
        print("냠냠..")

    def use_weapon(self):
        if self.gun != None:
            self.gun.fire()
        else:
            print("없네..당황.. ㅠㅜ")

p1 = Police("호돌이", "교통정리", "33")
p1.patrol()
p1.arrest("좀도둑")
p1.notify_mranda_rights()
p1.eat_donut()
# for i in range(25):
#     p1.fire()
# p1.reload()

g = Gun("m60리볼버", 8)
p = Police("포돌이","순경",20)
# p.receive_gun(g)
p.use_weapon()