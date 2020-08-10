# pip install pygame
import pygame

pygame.init()

# 화면크기
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 그리기
bg1 = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") #배경 이미지
bg2 = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") #배경 이미지
# 토끼
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/rabbit1.png")
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/rabbit2.png")
# 토끼사이즈
rabbit1 = pygame.transform.scale(rabbit1, (100,100))
rabbit2 = pygame.transform.scale(rabbit2, (100,100))

isRunning = True    # 게임을 계속 진행할지, 중지할지를 결정하는 변수
                    # flag성 변수

# 제목
pygame.display.set_caption("토끼 사냥")

# 토끼 위치 좌표
rx = 400
ry = 200
# 배경 좌표
bg1X = 0
bg2X = 1900
bgY = 0
cnt = 0
clock = pygame.time.Clock()

while isRunning:
    cnt += 1
    bg1X -= 2
    bg2X -= 2
    if bg1X == -1900: bg1X = 1900 
    if bg2X == -1900: bg2X = 1900
    # Frame 지정
    fps = clock.tick(60) # 화면의 초당 프레임 수 30
    # 프레임 확인
    # print("fps:"+str(clock.get_fps()))
    
    for event in pygame.event.get():    # 이벤트 모으기
        if event.type == pygame.QUIT:
            isRunning = False

    keys  = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] == 1:
        rx -= 5    
    if keys[pygame.K_UP] == 1:
        ry -= 5    
    if keys[pygame.K_RIGHT] == 1:
        rx += 5    
    if keys[pygame.K_DOWN] == 1:
        ry += 5
    
    if rx < 0: rx = 0
    if rx > screen_width - 100 : rx = screen_width - 100
    if ry < 0: ry = 0
    if ry > screen_height - 100 : ry = screen_height - 100


    # 배경 그리기
    screen.blit(bg1, (bg1X,bgY))
    screen.blit(bg2, (bg2X,bgY))
    if cnt%2 :
        screen.blit(rabbit1, (rx, ry))
    else:
        screen.blit(rabbit2, (rx, ry))

    pygame.display.update()     #게임화면 다시 그리기

pygame.quit()