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
        pygame.display.update()
        clock.tick(60)

startMenu()
gameLoop()
pygame.quit()
quit()