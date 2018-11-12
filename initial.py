import pygame
from Trivia import *

player_number = 0
intro = True
how_to = False
playnum_screen = False

pygame.init()

# Some snazzy 8 bit Jeopardy Music
# Music attributed to https://www.youtube.com/watch?v=gSnxvFCEwfE
mus = pygame.mixer.Sound('8bitJep.wav')
mus.play(-1)

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

'''
    Fonts used from magofonts: mago1, mago3
    Fonts attributed to: magodev
    https://magodev.itch.io/
'''

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
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("mago1.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def message_display(text):
    largeText = pygame.font.Font('mago3.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 

def startMenu():
    global intro
    global how_to
    global playnum_screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # clears display, blits title
    gameDisplay.fill(pink)
    largeText = pygame.font.Font('mago3.ttf', 100)
    mediumText = pygame.font.Font('mago3.ttf', 50)
    TextSurf, TextRect = text_objects("Trivia Game", largeText)
    TextRect.center = ((display_width/2),(display_height/2)-50)
    gameDisplay.blit(TextSurf, TextRect)

    # displays buttons that route to different functions
    button("Enter",250,450,100,50,green,lavender,howTo) # THIS GOES TO HOW TO() CORRECTLY.
    button("Quit",450,450,100,50,red,lavender,quit)

    pygame.display.update()
    clock.tick(40)


def howTo():
    global intro
    global how_to
    global playnum_screen
    intro = False
    how_to = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # displays title on screen
    gameDisplay.fill(pink)
    largeText = pygame.font.Font('mago3.ttf', 80)
    largemedText = pygame.font.Font('mago3.ttf', 60)
    mediumText = pygame.font.Font('mago3.ttf', 30)
    smallmedText = pygame.font.Font('mago3.ttf', 25)
    TextSurf, TextRect = text_objects("How To Play", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2)-200)
    gameDisplay.blit(TextSurf, TextRect)

    # text 1
    TextSurf1, TextRect1 = text_objects("Press 'Select Players' to select the number of players.", mediumText)
    TextRect1.center = ((display_width / 2), (display_height / 2) - 140)
    gameDisplay.blit(TextSurf1, TextRect1)

    # text 2
    TextSurf6, TextRect6 = text_objects("Use the keyboard to type a number from 1-4 and click 'Start'", mediumText)
    TextRect6.center = ((display_width / 2), (display_height / 2) - 100)
    gameDisplay.blit(TextSurf6, TextRect6)

    # text 2
    TextSurf2, TextRect2 = text_objects("Choose a question and use the keyboard to choose your answer", mediumText)
    TextRect2.center = ((display_width / 2), (display_height / 2) - 60)
    gameDisplay.blit(TextSurf2, TextRect2)

    # text 3
    TextSurf3, TextRect3 = text_objects("Click the screen or press enter to return to the game board", mediumText)
    TextRect3.center = ((display_width / 2), (display_height / 2) - 20)
    gameDisplay.blit(TextSurf3, TextRect3)

    # text 4
    TextSurf4, TextRect4 = text_objects("Pass the keyboard and mouse to the next player and continue playing", smallmedText)
    TextRect4.center = ((display_width / 2), (display_height / 2) + 20)
    gameDisplay.blit(TextSurf4, TextRect4)

    # text 5
    TextSurf5, TextRect5 = text_objects("First player to 1500 points wins!", largemedText)
    TextRect5.center = ((display_width / 2), (display_height / 2) + 80)
    gameDisplay.blit(TextSurf5, TextRect5)

    button("Select Players", 350, 500, 100, 50, green, lavender, numPlayers)


    pygame.display.update()
    clock.tick(40)

player_number = 1
setNumPlayers(player_number)

def numPlayers():
    global player_number
    global intro
    global how_to
    global playnum_screen
    how_to = False
    intro = False
    playnum_screen = True

    # displays title on screen
    gameDisplay.fill(pink)
    largeText = pygame.font.Font('mago3.ttf', 60)
    mediumText = pygame.font.Font('mago3.ttf', 50)
    TextSurf, TextRect = text_objects("Press '1-4'", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2) - 100)
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
                #print("1")
            elif event.key == pygame.K_2: 
                player_number = 2      
                #print("2")
            elif event.key == pygame.K_3:
                player_number = 3
                #print("3")
            elif event.key == pygame.K_4:
                player_number = 4
                #print("4")
            setNumPlayers(player_number)

    # displays number of players on screen
    TextSurf2, TextRect2 = text_objects("Number of Players: "+str(player_number), mediumText)
    TextRect2.center = ((display_width/2),(display_height/2)-30)     
    gameDisplay.blit(TextSurf2, TextRect2)

    # displays button that routes to game
    button("Start",350,450,100,50,green,lavender,main)

    pygame.display.update()
    clock.tick(40)


while intro:
    #print("intro")
    startMenu()
while how_to:
    #print("how to")
    howTo()
while playnum_screen:
    #print("player num screen")
    numPlayers()



