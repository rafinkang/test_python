import pygame
import random

pygame.init()

screen_width = 1200
screen_height = 800
# 배경 이미지 객체
bg = pygame.image.load("E:/dev/python_workspace/img/bg.jpg")
bg = pygame.transform.scale(bg, (1200, 800))
ball = pygame.image.load("E:/dev/python_workspace/img/gold.png")
ball = pygame.transform.scale(ball, (50, 50))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("핑퐁")

bx = 600
by = 400
inc_x = random.randint(-10, 10)
inc_y = random.randint(-10, 10)

# 시계변수
clock = pygame.time.Clock()

isRunning = True

def changeDirection(x, y, ix, iy):
    # 화면 윗쪽 벽에 맞으면 튕겨나가게 설정
    if y <= 3 or y >= screen_height-53:
        iy = -iy
    if x <= 3 or x >= screen_width-53:
        ix = -ix
    return ix, iy
    
while isRunning:
    bx -= inc_x
    by -= inc_y

    fps = clock.tick(30)
    
    inc_x, inc_y = changeDirection(bx, by, inc_x, inc_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    screen.blit(bg, (0, 0))
    screen.blit(ball, (bx, by))
    
    pygame.display.update()

pygame.quit()