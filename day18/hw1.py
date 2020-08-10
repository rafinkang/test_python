import pygame
import random
import math
pygame.init()

pygame.display.set_caption("고군분투")

screen_width = 800
screen_height = 500
score = 0
# font
pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS", 30)
screen = pygame.display.set_mode((screen_width, screen_height))

trapX1 = 950
trapX2 = 1050


bg1 = pygame.image.load("e:/dev/python_workspace/img/bg1.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/bg2.jpg")
bg1X = 0
bg2X = screen_width

run1 = pygame.image.load("e:/dev/python_workspace/img/run1.png")
run2 = pygame.image.load("e:/dev/python_workspace/img/run2.png")
run3 = pygame.image.load("e:/dev/python_workspace/img/run3.png")
run_list = [run1, run2, run3]
rx = 0
ry = 270

gold = pygame.image.load("e:/dev/python_workspace/img/gold.png")
silver = pygame.image.load("e:/dev/python_workspace/img/silver.png")

jump = False
jump_Y = 270
jump_status = 0

cnt = 0
clock = pygame.time.Clock()
isRunning = True

coinList = []
def makeCoin(coinObj, color):
    c = Coin(screen_width, random.randint(10, 260), coinObj, color)
    coinList.append(c)

def collision(x1, y1, x2, y2):
    dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    result = 0
    if dis < 50:
        result = 1
    return result

class Coin:
    def __init__(self, x, y, coinObj, color):
        self.x = x
        self.y = y
        self.coinObj = coinObj
        self.color = color
        
    def __del__(self):
        pass
        # print("코인 제거됨")
        

while isRunning:
    fps = clock.tick(60)
    
    bg1X -= 5
    bg2X -= 5
    if bg1X == -screen_width: bg1X = screen_width
    if bg2X == -screen_width: bg2X = screen_width
    screen.blit(bg1, (bg1X, 0))
    screen.blit(bg2, (bg2X, 0))

    
    
    cnt += 1
    screen.blit(run_list[(cnt//10)%3], (rx, ry))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            
    if rx < 0: rx = 0
    if rx > screen_width: rx = screen_width - 100
    
    # if rx >= bg2X+150 or rx <= bg2X+250 :
        
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] == 1: rx -= 5
    if keys[pygame.K_RIGHT] == 1: rx += 5
    if keys[pygame.K_SPACE] == 1: 
        jump = True
        jump_Y = ry - 100
        if jump_Y < 0: jump_Y = 0
        jump_status = 0
      
    if jump==True:
        if jump_status == 0: # up
            ry -= 10
            if jump_Y >= ry:
                ry = jump_Y
                jump_status = 1
        else: # down 
            ry += 10
            if 270 <= ry:
                ry = 270
                jump_status = 0
                jump_Y = 270
    
    if cnt%20 == 0:
        if (cnt//100)%2:
            makeCoin(gold, 'gold')
        else:
            makeCoin(silver, 'silver')
            
        
    for c in coinList:
        # print(c, c.x, c.y)
        screen.blit(c.coinObj, (c.x, c.y))
        c.x -= 5
        if c.x < -100:
            coinList.remove(c)
            del(c)
        
    for c in coinList:
        if collision(rx+50, ry+55, c.x, c.y) == 1:
            c.x = -150
            if c.color == 'gold':
                score += 20
            else:
                score += 10
    
    
    # print(score)
    txt = myFont.render("SCORE : "+str(score), False, (255, 0, 0))
    screen.blit(txt, (600, 20))
    pygame.display.update()
    

pygame.quit()