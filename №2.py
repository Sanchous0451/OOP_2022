import pygame
from pygame.draw import *

pygame.init()

FPS=30
screen = pygame.display.set_mode((400,400))


rect(screen,(255,228,181),(0,0,400,400),200)
rect(screen,(188,143,143),(0,250,400,400),200)
rect(screen,(255,239,213),(0,50,400,100),200)
circle(screen,(255,255,0),(200,100),35,100)
polygon(screen,(139,0,0),[(0,250),(30,200),(100,235),(115,220),(130,250)])
polygon(screen,(139,0,0),[(300,275),(310,200),(325,260),(350,175),(370,200),(400,275)])




pygame.display.update()
clock =pygame.time.Clock()
finished=False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished =True

pygame.quit