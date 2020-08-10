import pygame
import random
pygame.init()

pygame.display.set_caption("고군분투")

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

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
jump_cnt = 0

cnt = 0
clock = pygame.time.Clock()
isRunning = True
while isRunning:
    fps = clock.tick(30)
    
    bg1X -= 5
    bg2X -= 5
    if bg1X == -screen_width: bg1X = screen_width
    if bg2X == -screen_width: bg2X = screen_width
    screen.blit(bg1, (bg1X, 0))
    screen.blit(bg2, (bg2X, 0))

    cnt += 1
    screen.blit(run_list[cnt%3], (rx, ry))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            
    if rx < 0: rx = 0
    if rx > screen_width: rx = screen_width - 100
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] == 1: rx -= 5
    if keys[pygame.K_RIGHT] == 1: rx += 5
    if keys[pygame.K_SPACE] == 1: 
        jump = True
    
    if jump==True:
        if jump_cnt > 20:
            jump_cnt = 0
            jump = False
        elif jump_cnt > 10:
            ry += 10
        else:
            ry -= 10
        jump_cnt += 1
    
    if cnt%10 == 0:
        if (cnt//10)%2:
            #gold
            pass
            # screen.blit(gold, ())
        else:
            #silver
            pass
    
    
    pygame.display.update()
    

pygame.quit()