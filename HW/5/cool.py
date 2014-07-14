#cool.py

import pygame,sys #imports modules
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((600,400))
FPS = pygame.time.Clock()
pygame.display.set_caption("Cool stuff")

imgx = 10
imgy = 10

white=(255,255,255)
blue= (10,255,10)

while True:
    window.Surface.Obj.fill(white)
    pygame.draw.rect(display,blue,(imgx,imgy,imgx+30,imgy+30))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT):
                imgx -= 30
            elif event.key in (K_RIGHT):
                imgx += 30
            elif event.key in (K_UP):
                imgy -= 30
            elif event.key in (K_DOWN):
                imgy += 30
    pygame.display.update()
    fps.tick(30)
