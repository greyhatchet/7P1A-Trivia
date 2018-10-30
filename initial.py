import pygame

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

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    gameLoop()

def startMenu():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RETURN:
                    TextSurf, TextRect = text_objects("Enter number of players")
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
        pygame.display.update()
        clock.tick(15)