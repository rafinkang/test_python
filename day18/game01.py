# pip install pygame
import pygame
import random

pygame.init()

# 화면크기
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 그리기
bg = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") #배경 이미지
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/rabbit1.png")
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/rabbit2.png")

isRunning = True    # 게임을 계속 진행할지, 중지할지를 결정하는 변수
                    # flag성 변수
pygame.display.set_caption("토끼 사냥")

# 토끼 위치 좌표
rx = 400
ry = 200
cnt = 0
while isRunning:
    cnt += 1
    for event in pygame.event.get():    # 이벤트 모으기
        if event.type == pygame.QUIT:
            isRunning = False
    # 배경 그리기
    screen.blit(bg, (0,0))
    if cnt%2 :
        screen.blit(rabbit1, (rx, ry))
    else:
        screen.blit(rabbit2, (rx, ry))
    # rx = random.randint(1, 1200)
    # ry = random.randint(1, 800)
    pygame.display.update()     #게임화면 다시 그리기

pygame.quit()