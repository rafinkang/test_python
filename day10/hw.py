import time
class Marine:
    def __init__(self):
        self.name = '마린'
        self.hp = 100
        self.attackPoint = 4
        self.attackSpeed = 1
        self.type = 1
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
        self.name = "메딕"
        self.hp = 100
        self.x = 10
        self.y = 10
        self.mp = 100
        self.amor = 10
        self.healSize = 10
        self.type = 1

    def heal(self, other):
        if other.type != 1 : 
            print('인간만 치료가능')
            return False

        if other.hp < 100:
            other.hp += self.healSize
            if other.hp > 100: other.hp = 100
        else:
            return False
        print(other.name+"의 체력이 %d 만큼 회복되었습니다."%self.healSize)
        return True

# 1. Ghost  클래스를 생성 

#   Ghost 
class Ghost:
    def __init__(self):
        self.name = '고스트'
        self.hp = 100
        self.amor = 5
        self.attackPoint = 7
        self.type = 1
    
#   핵미사일발사() 
    def nuclear(self, other):
        other.hp = 0
        print('핵 발싸ㅏㅏㅏㅏ')

    def attack(self, other):
        other.hp -= self.attackPoint
        print('고스트가 ',other.name,'쏜다 빵야')

ma1 = Marine()
me1 = Medic()    
gh1 = Ghost()
gh2 = Ghost()

#   마린 ==> Ghost 공격 
ma1.attack(gh1)
#   메딕 ==> Ghost 치료 
me1.heal(gh1)
#   Ghost ==> 마린 
gh1.attack(ma1) 
#   Ghost ==> 메딕
gh1.attack(me1)
#   Ghost ==> Ghost
gh1.attack(gh2)

# 2. SiegeTank 
class siegeTank:
    def __init__(self):
        self.name = "씨즈탱크"
        self.mode = "normal"
        self.hp = 100
        self.attackPoint = 10
        self.attackRange = 10
        self.type = 2

#   SiegeMode() 
    def siegeMode(self):
        self.attackPoint += 10
        self.attackRange += 10
        print('시즈모드!')

    def attack(self, other):
        other.hp -= self.attackPoint
        print('시즈탱크 ',other.name,'공격! 부아앙')

si1 = siegeTank()
si1.siegeMode()

#   마린 ==> SiegeTank 공격 
ma1.attack(si1)
#   메딕 ==> SiegeTank 치료  XXXXXX 
me1.heal(si1)
#   Ghost ==> 마린 
gh1.attack(ma1)
#   Ghost ==> 메딕
gh1.attack(me1)
#   Ghost ==> Ghost
gh1.attack(gh2)
#   Ghost ==> SiegeTank 
gh1.attack(si1)
#  SiegeTank  ==> 마린
si1.attack(ma1)
#  SiegeTank  ==> 메딕 
si1.attack(me1)


# 3. Computer 객체를 생성할수 있는 클래스를 작성하세요 
# 	기능 : turnOn(), turnOff(), changeChannel(n) 

class Computer:
    def __init__(self):
        self.name = "컴퓨터"
        self.turn = "off"
        self.channel = 1
        self.volume = 1

    def turnOn(self):
        self.turn = "on"
        print("전원 On")
    
    def turnOff(self):
        self.turn = "off"
        print("전원 Off")

    def changeChannel(self, n):
        if self.turn == "off":
            print("전원이 꺼져있습니다.")
            return false
        self.channel = n
        print("채널 변경")

com1 = Computer()
com1.turnOn()
com1.changeChannel(10)
com1.turnOff()


# 5. 
# 	아래와 같은 코드가 실행될수 있도록 HandPhone 클래스를 작성하세요 

# 	hp = HandPhone()
# 	hp.call("010-1234-5678")  #011-1111-2222에서  010-1234-5678번으로 전화거는중 
# 	hp.phone_number= "010-1234-5678" # 011-1111-2222 에서 전화번호를 010-1234-5678 로변경함 
# 	hp.connect_internet() # 인터넷에 연결되었습니다. 
class HandPhone:
    def __init__(self):
        self.phone_number = "011-1111-2222"
        self.connect = False
    
    def call(self, number):
        print(self.phone_number,"에서",number,"로 전화거는중")

    def connect_internet(self):
        self.connect = True
        print("인터넷에 연결되었습니다.")
        

hp = HandPhone()

hp.call("010-1234-5678")
hp.phone_number = "010-1234-5678"
hp.connect_internet()