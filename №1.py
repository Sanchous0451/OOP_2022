import pygame
from pygame.draw import *

pygame.init()

FPS=30
screen = pygame.display.set_mode((400,400))


circle(screen,(0,0,0),(200,175),50,5)
circle(screen,(255,255,0),(200,175),49,100)
circle(screen,(255,0,0),(225,170),10,100)
circle(screen,(255,0,0),(175,170),10,100)
circle(screen,(0,0,0),(225,170),4,100)
circle(screen,(0,0,0),(175,170),4,100)
polygon(screen,(0,0,0),[(165,155),(180,165),(185,165),(185,165)],10)
polygon(screen,(0,0,0),[(235,155),(220,165),(215,165),(215,165)],10)
polygon(screen,(0,0,0),[(215,195),(215,195),(185,195),(185,195)],10)

pygame.display.update()
clock =pygame.time.Clock()
finished=False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished =True

pygame.quit