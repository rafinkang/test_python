import pygame
import math
import random 


# 초기화 
pygame.init()

# 미사일과 충돌 테스트 
def pythagoras(x1, y1, x2, y2):
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))




screen_width = 600
screen_height = 900

screen = pygame.display.set_mode((screen_width,screen_height))

isRunning = True

pygame.display.set_caption("우주 전쟁")

# 배경 이미지 객체 
bg1 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
# 이미지 크기를 화면의 크기로 변환
bg1 = pygame.transform.scale(bg1, (600,900))
bg2 = pygame.transform.scale(bg2, (600,900))


# 적 우주선 객체 


enemyShip1 = pygame.image.load("e:/dev/python_workspace/img/gunship0.png")
enemyShip2 = pygame.image.load("e:/dev/python_workspace/img/gunship1.png")
enemyShip3 = pygame.image.load("e:/dev/python_workspace/img/gunship2.png")
enemyShip4 = pygame.image.load("e:/dev/python_workspace/img/gunship3.png")
enemyShip1 = pygame.transform.scale(enemyShip1,(50,50))
enemyShip2 = pygame.transform.scale(enemyShip2,(50,50))
enemyShip3 = pygame.transform.scale(enemyShip3,(50,50))
enemyShip4 = pygame.transform.scale(enemyShip4,(50,50))



# 캐릭터 우주선 객체 

player1 = pygame.image.load("e:/dev/python_workspace/img/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/player4.png")
player1 = pygame.transform.scale(player1,(50,50))
player2 = pygame.transform.scale(player2,(50,50))
player3 = pygame.transform.scale(player3,(50,50))
player4 = pygame.transform.scale(player4,(50,50))

# 캐릭터 우주선 좌표 변수 

px = 250
py = 800


# 적 우주선 좌표 변수 
ex = 250
ey = 50



#카운터 변수 
cnt =0 
# 배경 y좌표 변수 
bg1Y = 0 
bg2Y = -900


# 시계 변수 
clock = pygame.time.Clock()


# 미사일 객체 
missile = pygame.image.load("e:/dev/python_workspace/img/missile1.png")

# 미사일 좌표 변수 
mx = -250
my = -300

#  미사일 리스트 
mList = []

#  적우주선  다량 출현 
enemyList = []

def makeEnemy():
    e = EnemyShip(random.randint(1,550), 50 ,100 , 1 )
    enemyList.append(e)


class EnemyShip:
    def __init__(self, x, y, hp, type):
        self.x = x
        self.y = y
        self.hp = hp # 기본 체력은 100  보스는 200
        self.type = type
        # type : 1 은 일반 적   2 : 보스 
    def __del__(self):
        print("적 제거됨")






# 충돌 체크 함수 
def collision (x1, y1, x2, y2):
    dis = pythagoras(x1, y1, x2, y2)
    result = 0 
    if dis < 30:
        result = 1
    return result



class Missile:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
    
    def __del__ (self):
        pass
#        print("소멸자.. 미사일 제거됨")




#여기 사이의 코드가 반복 
while isRunning :
    cnt +=1
    bg1Y += 2 
    bg2Y += 2 

    my -= 3

    ey += 3

    if bg1Y >900:
        bg1Y = -900
        bg2Y = 0
    if bg2Y >900:
        bg2Y = -900
        bg1Y = 0
    # frame 지정
    fps = clock.tick(30) # 화면에 초당 프레임수 30 

    # 현재 프레임이 얼마인지 확인
    # print("fps : " , str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("마우스 클릭됨")
            mx , my = pygame.mouse.get_pos()
            mList.append(Missile(mx, my))

    #print(mList)

    # 적 우주선 객체 생성 
    if cnt % 10 == 0: 
        makeEnemy()

    # 배경 그리기 
    screen.blit(bg1,(0,bg1Y))            
    screen.blit(bg2,(0,bg2Y))    

    #마우스 좌표 구하기 
    #print(pygame.mouse.get_pos())
    px , py = pygame.mouse.get_pos()

    # 미사일 그리기 
    for m in mList:
        screen.blit(missile,(m.x, m.y))
        m.y -= 5
        if m.y <= -50:
            mList.remove(m)
            del(m)

    # 미사일과 적우주선간 충돌 발생 여부 체크 하는 함수를 호출
    
    for m in mList:
        for e in enemyList:
            result = collision(e.x, e.y, m.x, m.y)
            if result == 1:
                e.y -= 10  # 적은 약간 뒤로 밀기
                m.y = -100 # 미사일 화면밖으로 뿅~
                e.hp -= 50 # 적 체력 50 감소 
            
            if e.hp <= 0:
                e.y = 950 # 화면 밖으로 내보내기 
                # 죽은걸로 처리 
                enemyList.remove(e)
                del(e)


    for e in enemyList:
        if cnt % 4 == 0:
            screen.blit(enemyShip1, (e.x-25,e.y-25))
        elif cnt % 4 == 1:
            screen.blit(enemyShip2, (e.x-25,e.y-25))
        elif cnt % 4 == 2:
            screen.blit(enemyShip3, (e.x-25,e.y-25))
        elif cnt % 4 == 3:
            screen.blit(enemyShip4, (e.x-25,e.y-25))
        e.y+=3
        # 적 비행기가 화면 밖으로 나가면 제거 
        if e.y >= 950:
            enemyList.remove(e)
            del(e)

    if cnt % 4 == 0:
        screen.blit(player1,(px-25,py-25))            
    elif cnt % 4 == 1:
        screen.blit(player2,(px-25,py-25))            
    elif cnt % 4 == 2:
        screen.blit(player3,(px-25,py-25))            
    elif cnt % 4 == 3:
        screen.blit(player4,(px-25,py-25))            
    pygame.display.update()

pygame.quit()