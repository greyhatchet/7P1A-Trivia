import pygame
#from gameLoop import *

player_number = 0
intro = True
playnum_screen = False

pygame.init()
 
infoObject = pygame.display.Info()
display_width = infoObject.current_w - 100
display_height = infoObject.current_h - 100

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Trivia Game')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
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
            
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    mediumText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects("Trivia Game", largeText)
    TextSurf2, TextRect2 = text_objects("Press 'Enter' to Start", mediumText)
    TextRect.center = ((display_width/2),(display_height/2)-100)
    TextRect2.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(TextSurf2, TextRect2)

    button("GO!",450,450,100,50,white,black,numPlayers)
    button("Quit",650,450,100,50,red,black,quit)

    pygame.display.update()
    clock.tick(15)


def numPlayers():
    global player_number
    global intro
    global playnum_screen
    intro = False
    playnum_screen = True
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects("Enter number of players", largeText)
    TextRect.center = ((display_width/2),(display_height/2)-100)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


#startMenu()
while intro:
    startMenu()
while playnum_screen:
    numPlayers()
#gameLoop()
pygame.quit()
quit()