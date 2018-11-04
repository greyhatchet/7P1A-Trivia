import os, sys
import pygame
from pygame.locals import *
import unittest

#Unit test for the creation of player class
class testPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("1")

    def testInits(self):
        self.assertEqual(self.player.points, 0)
        self.assertEqual(self.player.name, "1")

# Class defining a Player, initializes with 0 points and user defined name
class Player:
    def __init__(self, name):
        self.points = 0
        self.name = name

# When player object printed, name returned
    def __str__(self):
        return self.name

# Class of Question, contains user defined attributes q(question string) and a (answer string)
class Question:
    def __init__(self, q, a):
        self.q = q
        self.a = a

#When Question object printed, return Q: "Question"
#                                     A: "Answer"
    def __str__(self):
        return "Q: %s\nA: %s" % (self.q, self.a)


#Initialize tuples for use as screen colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Initialize variables used to notify program of current game state
GAMEBOARD = 'gameboard'
QUESTION = 'question'
ANSWER = 'answer'


class Jeopardy:

    # qm attribute (dictionary storing *** )
    qm = {}

    # board attribute (list storing the keys to qm dictionary)
    board = []

    # Current mode is displaying the gameboard
    mode = GAMEBOARD

    curQ = None

    def __init__(self, screen, questionFile, round=1):
        self.screen = screen

        # load fonts
        self.smallFont = pygame.font.Font(None, 48)
        self.bigFont = pygame.font.Font(None, 80)

        # load questions from text file
        self.loadQuestions(questionFile)

        # create gameboard w/ list of keys
        self.board.append(list(self.qm.keys()))

        # appends list w/ length 6 of current point * round # total to board 
        for p in range(100, 501, 100):
            self.board.append([p * round] * 6)

    def loadQuestions(self, filename):
        f = open(filename)
        lines = f.readlines()
        # strip white spaces and split on colons
        for line in lines:
            data = line.strip().split(':')
        # input category, points, question, and answer as tuple into addQuestion function
            self.addQuestion(*data)

    def addQuestion(self, category, points, q, a):

        # check if category key in dictionary
        if not category in self.qm.keys():

        #if not, append category input as key into list and the value an empty dictionary
            self.qm[category] = {}

        #assign second dictionary's key to the point variable, and the value to a question object 
        self.qm[category][points] = Question(q, a)


    def mouseClick(self, pos):
        # if current mode is gameboard
        if self.mode == GAMEBOARD:

            #ask the appropriate question depending on the click position
            self.askQuestion(pos[0] / 133, pos[1] / 100)

        #if looking at question & screen clicked, reveal answer (*** need to change for multiple choice ***)
        elif self.mode == QUESTION:
            self.mode = ANSWER

        #if looking at answer & screen clicked, return to gameboard
        elif self.mode == ANSWER:
            self.mode = GAMEBOARD

    def askQuestion(self, col, row):
        q = None
        # if valid screen position selected continue
        if row != 0:
            # variable indexes to the key for the column chosen by click (CATEGORY)
            cat = self.board[0][int(col)]
            # variable contains string with the appropriate point total for the selected question (POINTS)
            points = str(self.board[int(row)][int(col)])
            # if valid screen position selected continue
            if points != '':
                #indexes to current question object
                self.curQ = self.qm[cat][points]

                #label board location as used
                self.board[int(row)][int(col)] = ''

                #set current mode to question
                self.mode = QUESTION

    def drawTextCentered(self, str, skiperoo=-75):
        choperoo = len(str)

        font = self.smallFont

        # render string and compare length to screen width
        text = font.render(str, 1, WHITE)

        # if string too long, break up at first space in the last half of the string
        while text.get_rect().width > self.screen.get_rect().width:
            for c in range(int(choperoo / 2), choperoo):
                if str[c] == ' ':
                    choperoo = c
                    break

            # render first part of string
            text = font.render(str[:choperoo], 1, WHITE)

        # cr is first part of string get_rect() object
        cr = text.get_rect()

        #center of text is placed in the center of the screen
        cr.center = self.screen.get_rect().center

        #y coordinate shifted the value inputted (defaults to 75 pixels down)
        cr.y += skiperoo

        # blit text in appropiate position
        self.screen.blit(text, cr)

        #if string needed to be chopped, call function recursively w/ remainder of string
        if choperoo != len(str):
            self.drawTextCentered(str[choperoo:], skiperoo + cr.height)

    def draw(self):
        #display functions depending on game state
        if self.mode == GAMEBOARD:
            self.drawBoard()
        elif self.mode == QUESTION:
            self.drawTextCentered(self.curQ.q)
        elif self.mode == ANSWER:
            self.drawTextCentered(self.curQ.a)

    def drawBoard(self):
        #grid display
        xStart, xEnd = 0, 800
        yStart, yEnd = 0, 600
        xStep = xEnd // 6
        yStep = yEnd // 6

        # Display black lines outlining grid in appropriate locations
        for x in range(xStart, xEnd + 1, xStep):
            pygame.draw.line(self.screen, BLACK, (x, yStart), (x, yEnd), 5)
        for y in range(yStart, yEnd + 1, yStep):
            pygame.draw.line(self.screen, BLACK, (xStart, y), (xEnd, y), 5)

        # display text in boxes
        for x in range(0, 6):

            #display column (category) title
            text = self.smallFont.render(self.board[0][x], 1, WHITE)
            self.screen.blit(text, (x * xStep + 10, 25))

            for y in range(1, 6):
                #display point total
                text = self.bigFont.render(str(self.board[y][x]), 1, WHITE)
                self.screen.blit(text, (x * xStep + 7, y * yStep + 10))


def main():
    # initialize pygame, screen, and caption
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Jeopardy')

    # mouse set to be monitored
    pygame.mouse.set_visible(1)
    # fill background with blue and update (flip)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 200))
    pygame.display.flip()
    # allsprites = pygame.sprite.renderPlain((fist, chimp))
    clock = pygame.time.Clock()

    # initialize jeopardy class at round 1 & input file
    jeopardy = Jeopardy(screen, 'round1.txt')

    # round 2
    #jeopardy = Jeopardy(screen, 'round2.txt', 2)

    #game loop
    quit = False
    while not quit:
        #framerate
        clock.tick(60)

        #event handler (X out and escape quit the game)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                quit = True

            # on mouse click, call mouseClick function to interpret column & point selection
            elif event.type == MOUSEBUTTONDOWN:
                jeopardy.mouseClick(pygame.mouse.get_pos())

        #blit background clean, call jeopardy draw function depending on game state, update display
        screen.blit(background, (0, 0))
        jeopardy.draw()
        pygame.display.flip()


if __name__ == '__main__':
    main()
