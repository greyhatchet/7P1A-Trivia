import pygame
from Trivia import *

player_number = 0
intro = True
playnum_screen = False

pygame.init()
 
# size of display screen
display_width = 800 
display_height = 700 

# available colors
black = (0,0,0)
white = (255,255,255)
#red = (255,0,0)
green = (60,179,113)
blue = (0, 0, 200)
pink = (255,192,203)
lavender = (221,160,221)
red = (205,92,92)

# sets display, caption, and clock
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Trivia Game')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 

def startMenu():
    global intro
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # clears display, blits title
    gameDisplay.fill(pink)
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    mediumText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects("Trivia Game", largeText)
    TextRect.center = ((display_width/2),(display_height/2)-100)
    gameDisplay.blit(TextSurf, TextRect)

    # displays buttons that route to different functions
    button("Enter",250,450,100,50,green,lavender,numPlayers)
    button("Quit",450,450,100,50,red,lavender,quit)

    pygame.display.update()
    clock.tick(15)

player_number = 1

def numPlayers():
    global player_number
    global intro
    global playnum_screen
    intro = False
    playnum_screen = True
    
    # displays title on screen 
    gameDisplay.fill(pink)
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    mediumText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects("Press '1-4'", largeText)
    TextRect.center = ((display_width/2),(display_height/2)-100)
    gameDisplay.blit(TextSurf, TextRect)

    # assigns functions with keys 
    # quit, ends game
    # 1-4 assigns global variable player_number
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player_number = 1
                print("1")
            elif event.key == pygame.K_2: 
                player_number = 2      
                print("2")     
            elif event.key == pygame.K_3:
                player_number = 3
                print("3")
            elif event.key == pygame.K_4:
                player_number = 4
                print("4")
            setNumPlayers(player_number)
    
    # displays number of players on screen 
    TextSurf2, TextRect2 = text_objects("Number of Players: "+str(player_number), mediumText)
    TextRect2.center = ((display_width/2),(display_height/2)-30)     
    gameDisplay.blit(TextSurf2, TextRect2)

    # displays button that routes to game
    button("Start",350,450,100,50,green,lavender,main)

    pygame.display.update()
    clock.tick(15)


while intro:
    startMenu()
while playnum_screen:
    numPlayers()

pygame.quit()
quit()
