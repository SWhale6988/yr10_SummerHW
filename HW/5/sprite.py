import pygame,sys,time  #Imports the pygame module and the sys module for exiting the program
#imports time for pauses
pygame.init() #Initializes pygame

screen = pygame.display.set_mode([750, 750]) #Creates canvas
w = pygame.Color("white") #Declares variables for the sprite(s)
b = pygame.Color("black")

frame1 = [                  #Declares the first frame row by row
[b,b,w,b,b,b,b,b,w,b,b],
[b,b,b,w,b,b,b,w,b,b,b],
[b,b,w,w,w,w,w,w,w,b,b],
[b,w,w,b,w,w,w,b,w,w,b],
[w,w,w,w,w,w,w,w,w,w,w],
[w,b,w,w,w,w,w,w,w,b,w],
[w,b,w,b,b,b,b,b,w,b,w],
[b,b,b,w,w,b,w,w,b,b,b],


    ]



frame2 = [                  #Declares the second frame row by row
[b,b,b,b,w,b,w,b,b,b,b],
[b,b,b,w,b,b,b,w,b,b,b],
[b,b,w,w,w,w,w,w,w,b,b],
[b,w,w,b,w,w,w,b,w,w,b],
[w,w,w,w,w,w,w,w,w,w,w],
[w,b,w,w,w,w,w,w,w,b,w],
[w,b,w,b,b,b,b,b,w,b,w],
[b,b,w,w,b,b,b,w,w,b,b],


    ]
def draw_frame(surface,data):
    for y, row in enumerate(data): #Mentions each item in the list one by one
        for x, colour in enumerate(row): 
            rect = pygame.Rect(x*15, y*15, 15, 15) #Defines pixel size
            screen.fill(colour, rect=rect) #outputs sprite



while True:
    for event in pygame.event.get():  #Lets the user wuit the game
        if event.type == pygame.QUIT:
            sys.exit #Exits

    draw_frame(screen,frame1) #Displays first frame
    pygame.display.update() #Updates screen
    pygame.time.wait(500) #Waits 500ms
    
    draw_frame(screen,frame2) #displays second frame
    pygame.display.update()#Updates screen
    pygame.time.wait(500) #waits 500ms
