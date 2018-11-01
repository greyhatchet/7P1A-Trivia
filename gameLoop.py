import pygame
import time
import random
from initial import *

def gameLoop():
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
               quit()
            #elif event.type == pygame.MOUSEBUTTONDOWN:
                #jeopardy.mouseClick(pygame.mouse.get_pos())
        pygame.display.update()
        clock.tick(60)

#while intro:
    #startMenu()
#hile playnum_screen:
    #numPlayers()
#gameLoop()
pygame.quit()
quit()