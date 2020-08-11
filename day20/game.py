import pygame
import random
import math
import os
# 창밖으로 안튀기게
os.environ['SDL_VIDEO_WINDOW_POS']="50,50"

pygame.init()

screen_width = 1200
screen_height = 800
# 배경 이미지 객체
bg = pygame.image.load("E:/dev/python_workspace/img/bg.jpg")
bg = pygame.transform.scale(bg, (1200, 800))
ball = pygame.image.load("E:/dev/python_workspace/img/gold.png")
ball_w = 50
ball_h = 50
ball = pygame.transform.scale(ball, (ball_w, ball_h))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("핑퐁")

bx = 600
by = 700
inc_x = random.randint(-10, 10)
inc_y = random.randint(-10, 10)
# inc_x = 20
# inc_y = 10

# 시계변수
clock = pygame.time.Clock()

isRunning = True

def changeDirection(x, y, ix, iy):
    # 화면 윗쪽 벽에 맞으면 튕겨나가게 설정
    # if y <= 3 or y >= screen_height-ball_h-3:
    if y <= 3 :
        iy = -iy
    if x <= 3 or x >= screen_width-ball_w/2-3:
        ix = -ix
    return ix, iy

def changeDirection2(x, y, ix, iy, block):
    result = False
    if (x == block.x and block.y <= y <= block.y + block.height) or (x == block.x + block.width and block.y <= y <= block.y + block.height):
        ix = -ix
        result = True
    elif (y == block.y and block.x <= x <= block.x + block.width) or (y == block.y + block.height and block.x <= x <= block.x + block.width):
        iy = -iy
        result = True
    
    return ix, iy, result



# Define the colors we will use in RGB format
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)

colorList = [BLACK, WHITE, BLUE, GREEN, RED]
blockList = []
class Block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def __del__(self):
        print("블록 삭제됨")

def makeBlock(width, height):
    # 1200 -> 100 / 12칸 
    # 800 -> 200~300 -> 50 / 6칸
    for h in range(screen_height//2//height):
        for w in range(screen_width // width):
            rnd = random.randint(0,4)
            if rnd != 0:
                blockList.append(Block(w*width, h*height, width, height,colorList[rnd]))

makeBlock(100, 50)
barX = 500
while isRunning:
    bx -= inc_x
    by -= inc_y

    fps = clock.tick(60)
    
    inc_x, inc_y = changeDirection(bx, by, inc_x, inc_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    barX, barY = pygame.mouse.get_pos()
    screen.blit(bg, (0, 0))
    screen.blit(ball, (bx-ball_w/2, by-ball_h/2))
    # 박스 그리기
    for b in blockList:
        pygame.draw.rect(screen, b.color, [b.x, b.y, b.width, b.height])
    
    for b in blockList:
        inc_x, inc_y, res = changeDirection2(bx, by, inc_x, inc_y, b)
        if res:
            blockList.remove(b)
            del(b)
            break
        
    
    bar = pygame.draw.rect(screen, (0,0,0), [barX, 750, 200, 20])
    
    if by == 750-ball_h/2 and barX <= bx <= barX + 200:
        inc_y = -inc_y

    
    pygame.display.update()

pygame.quit()