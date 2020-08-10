# 게임의 기본틀
import pygame

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
    
    # 플레이어 그리기
    if cnt % 4 ==0:
        screen.blit(player1, (playerX - 25, playerY - 25))
    elif cnt % 4 == 1:
        screen.blit(player2, (playerX - 25, playerY - 25))
    elif cnt % 4 == 2:
        screen.blit(player3, (playerX - 25, playerY - 25))
    elif cnt % 4 == 3:
        screen.blit(player4, (playerX - 25, playerY - 25))
    
    # 적군 그리기
    gunshipY += 3
    if cnt % 4 ==0:
        screen.blit(gunship0, (gunshipX - 25, gunshipY - 25))
    elif cnt % 4 == 1:
        screen.blit(gunship1, (gunshipX - 25, gunshipY - 25))
    elif cnt % 4 == 2:
        screen.blit(gunship2, (gunshipX - 25, gunshipY - 25))
    elif cnt % 4 == 3:
        screen.blit(gunship3, (gunshipX - 25, gunshipY - 25))

    pygame.display.update()

pygame.quit()