import pygame
import random

pygame.init()

screen_width = 1200
screen_height = 800
# 배경 이미지 객체
bg = pygame.image.load("E:/dev/python_workspace/img/bg.jpg")
bg = pygame.transform.scale(bg, (1200, 800))
ball = pygame.image.load("E:/dev/python_workspace/img/gold.png")
ball = pygame.transform.scale(ball, (100, 100))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("핑퐁")

bx = 600
by = 400
inc_x = random.randint(-10, 10)
inc_y = random.randint(-10, 10)

isRunning = True
while isRunning:
    bx -= inc_x
    by -= inc_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    screen.blit(bg, (0, 0))
    screen.blit(ball, (bx, by))
    
    pygame.display.update()

pygame.quit()