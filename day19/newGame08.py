# 게임의 기본틀
import pygame
import math
import random
# 초기화
pygame.init()

            
screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("우주 전쟁")
isRunning = True

# 배경 이미지 객체
bg = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
# 이미지 크기를 화면의 크기로 변환
bg = pygame.transform.scale(bg, (600, 900))
# print(bg) # <Surface(576x869x24 SW)>
bgX = 0
bgY = 0

# 적 우주선 출현
gunship0 = pygame.image.load("e:/dev/python_workspace/img/gunship0.png")
gunship1 = pygame.image.load("e:/dev/python_workspace/img/gunship1.png")
gunship2 = pygame.image.load("e:/dev/python_workspace/img/gunship2.png")
gunship3 = pygame.image.load("e:/dev/python_workspace/img/gunship3.png")
gunship0 = pygame.transform.scale(gunship0,(50, 50))
gunship1 = pygame.transform.scale(gunship1,(50, 50))
gunship2 = pygame.transform.scale(gunship2,(50, 50))
gunship3 = pygame.transform.scale(gunship3,(50, 50))
gunshipX = 300
gunshipY = 0
enemyList = []
# 플레이어
player1 = pygame.image.load("e:/dev/python_workspace/img/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/player4.png")
player1 = pygame.transform.scale(player1,(50, 50))
player2 = pygame.transform.scale(player2,(50, 50))
player3 = pygame.transform.scale(player3,(50, 50))
player4 = pygame.transform.scale(player4,(50, 50))
# 플레이어 좌표
playerX = 300
playerY = 800

# 미사일
missile = pygame.image.load("e:/dev/python_workspace/img/missile1.png")
missileList = []
# 시계변수
clock = pygame.time.Clock()

cnt = 0


# 적 미사일과 충돌 테스트
def pytagoras(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# 충돌 체크 함수
def collision(x1, y1, x2, y2):
    dis = pytagoras(x1, y1, x2, y2)
    result = 0
    if dis < 30:
        result = 1
    return result

def mekeEnemy():
    # e = EnemyShip(x, y, hp, type)
    e = EnemyShip(random.randint(1,550), 50, 100, 1)
    enemyList.append(e)
    

class EnemyShip:
    def __init__(self, x, y, hp, type):
        self.x = x
        self.y = y
        self.hp = hp
        # 기본 100, 보스:200
        self.type = type 
        # type 1: 일반 2: 보스
    
    def __del__(self):
        print("적 제거됨")

class Missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __del__(self):
        pass
        # print("소멸자 - 미사일객체 제거됨")
        

while isRunning:
    cnt += 1
    # 화면에 초당 프레임을 30으로
    fps = clock.tick(60)
    # 현재 프레임 확인
    # print("fps : ", str(clock.get_fps()))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("마우스 클릭 됨")
            missileX, missileY = pygame.mouse.get_pos()
            missileList.append(Missile(missileX, missileY))
            
        
    # 배경 그리기
    bgY += 2
    screen.blit(bg, (bgX, bgY))
    screen.blit(bg, (bgX, -screen_height + bgY))
    if bgY == screen_height:
        bgY = 0
        
    # 마우스 좌표 구하기
    # print(pygame.mouse.get_pos())
    playerX, playerY = pygame.mouse.get_pos()

    # 미사일 그리기
    for m in missileList:
        screen.blit(missile, (m.x, m.y))
        m.y -= 5
        if m.y < -50: 
            missileList.remove(m)
            del(m)
            
    # 미사일과 적 우주선간 충돌 발생 여부 체크하는 함수를 호출
    for m in missileList:
        for e in enemyList:
            result = collision(e.x, e.y, m.x, m.y)
            if result == 1:
                e.y -= 10   #적은 살짝 뒤로
                m.y = -100  #미사일은 화면 밖으로
                e.hp -= 50  #적 체력 50감소

                if e.hp <= 0:
                    e.y = 950 #죽었으면 화면 밖으로 내보내기
                    # 죽은거로 처리
                    missileList.remove(m)
                    del(e)                
    
    
    if cnt % 20 == 0:
        mekeEnemy()
    # 적군 그리기
    for e in enemyList:
        if cnt % 4 ==0:
            screen.blit(gunship0, (e.x - 25, e.y - 25))
        elif cnt % 4 == 1:
            screen.blit(gunship1, (e.x - 25, e.y - 25))
        elif cnt % 4 == 2:
            screen.blit(gunship2, (e.x - 25, e.y - 25))
        elif cnt % 4 == 3:
            screen.blit(gunship3, (e.x - 25, e.y - 25))
            
        e.y += 3
        if e.y > 950:
            enemyList.remove(e)
            del(e)

    # 플레이어 그리기
    if cnt % 4 ==0:
        screen.blit(player1, (playerX - 25, playerY - 25))
    elif cnt % 4 == 1:
        screen.blit(player2, (playerX - 25, playerY - 25))
    elif cnt % 4 == 2:
        screen.blit(player3, (playerX - 25, playerY - 25))
    elif cnt % 4 == 3:
        screen.blit(player4, (playerX - 25, playerY - 25))
    

    pygame.display.update()

pygame.quit()