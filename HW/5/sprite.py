#paste code here
import pygame,sys #Imports modules

pygame.init() #Initialises pygame

screen = pygame.display.set_mode([225, 150]) #creates canvas
w = pygame.Color("white") #Declares colours
b = pygame.Color("black")

data = [ #declares sprite
[b,b,w,b,b,b,b,b,w,b,b],
[b,b,b,w,b,b,b,w,b,b,b],
[b,b,w,w,w,w,w,w,w,b,b],
[b,w,w,b,w,w,w,b,w,w,b],
[w,w,w,w,w,w,w,w,w,w,w],
[w,b,w,w,w,w,w,w,w,b,w],
[w,b,w,b,b,b,b,b,w,b,w],
[b,b,b,w,w,b,w,w,b,b,b],


    ]

for y, row in enumerate(data): #mentions each item one by one
    for x, colour in enumerate(row):
        rect = pygame.Rect(x*15, y*15, 15, 15)
        screen.fill(colour, rect=rect) #outputs sprite

pygame.display.update() #Updates screen

while True: #Quits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
