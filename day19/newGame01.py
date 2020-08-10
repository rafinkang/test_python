# 게임의 기본틀
import pygame

# 초기화
pygame.init()

screen_width = 600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("우주 전쟁")
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        
    pygame.display.update()

pygame.quit()