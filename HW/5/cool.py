#cool.py
#Moves a blue rectangle around the screen
#Use WASD or arrow keys to move character
import pygame,sys #imports modules
from pygame.locals import * #imports a libary of pygame

pygame.init() #initialises pygame
display = pygame.display.set_mode((600,400)) #creates a pygame window
FPS = pygame.time.Clock() #Sets up a clock
pygame.display.set_caption("Cool stuff") #Sets window title
imgx = 10 #x/y variables for the character
imgy = 10

white=(255,255,255) #Declares colours
blue= (10,255,10)
display.fill(white)
while True: #main loop
    pygame.draw.rect(display,blue,(imgx,imgy,imgx+30,imgy+30))#Draws a square based on imgy and imgx

    for event in pygame.event.get(): #checks for events
        if event.type == QUIT: #If player wants to quit..
            pygame.quit #..stops pygame
            sys.exit #Exits the window
        elif event.type == KEYDOWN: #If there is a key down..
            if event.key in (K_LEFT,K_a): #If the key is left or d
                imgx -= 30 #Moves character left
            elif event.key in (K_RIGHT,K_d): #If the key is right or a
                imgx += 30 #moves character right
            elif event.key in (K_UP,K_w): #If the key  is up or w
                imgy -= 30 #moves character up
            elif event.key in (K_DOWN,K_s): #If the key is down or s
                imgy += 30 #Moves character down
    pygame.display.update() #Updates screen
    #clock.tick(30) #FPS tick (30 FPS)
