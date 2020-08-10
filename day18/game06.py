# pip install pygame
import pygame
import math

pygame.init()

# 토끼의 중심좌표와 마우스 클릭위치의 거리 구하기
def pythagoras(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# 배경음악
# pygame.mixer.music.load("e:/dev/python_workspace/sounds/backsound.mp3")
# pygame.mixer.music.set_volume(1)   #1~0.1
# pygame.mixer.music.play(1)

# 제목
pygame.display.set_caption("토끼 사냥")
# 화면크기
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

# # 총소리 사운드 객체
# fSound = pygame.mixer.Sound("e:/dev/python_workspace/sounds/fire.wav")
# fSound.set_volume(1)
# fSound.play()
# # 비명 사운드 객체
# sSound = pygame.mixer.Sound("e:/dev/python_workspace/sounds/scream.wav")
# sSound.set_volume(1)
# sSound.play()
# 배경 그리기
bg1 = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") #배경 이미지
bg2 = pygame.image.load("e:/dev/python_workspace/img/bg.jpg") #배경 이미지
# 토끼
rabbit1 = pygame.image.load("e:/dev/python_workspace/img/rabbit1.png")
rabbit2 = pygame.image.load("e:/dev/python_workspace/img/rabbit2.png")
# 토끼사이즈
rabbit1 = pygame.transform.scale(rabbit1, (100,100))
rabbit2 = pygame.transform.scale(rabbit2, (100,100))
# 조준경
snipe = pygame.image.load("e:/dev/python_workspace/img/snipe.png")
snipe = pygame.transform.scale(snipe, (100,100))
# 총알구멍
hole = pygame.image.load("e:/dev/python_workspace/img/hole.png")
hole = pygame.transform.scale(hole, (10,10))

# 총알구멍 위치
holeX = 0
holeY = 0
# 조준경 위치
snipeX = 300
snipeY = 300
# 토끼 위치 좌표
rx = 400
ry = 200
# 배경 좌표
bg1X = 0
bg2X = 1900
bgY = 0
cnt = 0
clock = pygame.time.Clock()
isRunning = True    # 게임을 계속 진행할지, 중지할지를 결정하는 변수
                    # flag성 변수
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
            
        if event.type == pygame.MOUSEBUTTONUP:
            # fSound.play()
            holeX, holeY = pygame.mouse.get_pos()
            dis = pythagoras(holeX, holeY, rx+50, ry+50)
            # print(dis)
            if dis < 50:
                print("사냥성공!")
    # print(pygame.mouse.get_pressed())
    # mouses = pygame.mouse.get_pressed()
    # print(pygame.mouse.get_pos()) # return tuple
    snipeX, snipeY = pygame.mouse.get_pos()
    
    # if mouses[0] == 1:
    #     print("좌클릭")
    
    
    keys  = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] == 1 and 0 <= rx-5 <= screen_width-100:
        rx -= 5    
    if keys[pygame.K_UP] == 1 and 0 <= ry-5 <= screen_height-100:
        ry -= 5    
    if keys[pygame.K_RIGHT] == 1 and 0 <= rx+5 <= screen_width-100:
        rx += 5    
    if keys[pygame.K_DOWN] == 1 and 0 <= ry+5 <= screen_height-100:
        ry += 5

    # if keys[pygame.K_1] == 1:
    #     pygame.mixer.music.stop()
    # elif keys[pygame.K_2] == 1:
    #     pygame.mixer.music.play()
        


    # 배경 그리기
    screen.blit(bg1, (bg1X,bgY))
    screen.blit(bg2, (bg2X,bgY))
    if cnt%2 :
        screen.blit(rabbit1, (rx, ry))
    else:
        screen.blit(rabbit2, (rx, ry))
        
    screen.blit(hole, (holeX-5,holeY-5))
        
    screen.blit(snipe, (snipeX-50, snipeY-50))

    pygame.display.update()     #게임화면 다시 그리기

pygame.quit()