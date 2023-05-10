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
polygon(screen,(139,69,0),[(0,400),(25,320),(30,200),(40,150),(60,240),(80,350),(90,300),(120,270),(135,320),(150,400)])
polygon(screen,(139,69,0),[(270,400),(280,360),(300,325),(315,355),(335,300),(340,250),(350,190),(360,270),(375,325),(390,380),(400,400)])
polygon(screen, (0,0,0),[(150,155),(140,135),(155,155)])
polygon(screen,(0,0,0),[(150,155),(160,135),(155,155)])
polygon(screen, (0,0,0),[(190,170),(170,150),(195,170)])
polygon(screen,(0,0,0),[(190,170),(210,150),(195,170)])
polygon(screen, (0,0,0),[(160,190),(145,170),(170,190)])
polygon(screen,(0,0,0),[(160,190),(185,170),(170,190)])



pygame.display.update()
clock =pygame.time.Clock()
finished=False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished =True

pygame.quit