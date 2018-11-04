import os, sys
import pygame
from pygame.locals import *
from question_reader import *
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

    def __str__(self):
        return self.name

    def addPoints(self, score):
        self.points += score

    def getScore(self):
        return self.point


category_list = ['test0', 'test1', 'test2', 'test3', 'test4', 'test5']
num_questions = 6 # Number of questions per category

class MCQuestion:
    def __init__(self, q, a_list, a_num, value):
        self.q = q
        self.a_list = a_list
        self.a_num = int(a_num)
        self.value = value

    def __str__(self):
        self_str = "Q: " + self.q + "\n\n"
        for i in range(len(self.a_list)):
            self_str += str(i+1) + ": " + self.a_list[i] + "\n"
        return self_str

    def getAnsNum(self):
        return self.a_num

    def getValue(self):
        return self.value

    def getAnswer(self):
        ans_str = str(self.a_num + 1) + ": " + self.a_list[self.a_num]
        return ans_str

class TFQuestion:
    def __init__(self, q, a, value):
        self.q = q
        self.a = a
        self.value = value

    def __str__(self):
        self_str = "Q: " + self.q + "\n1: True\n2: False"
        return self_str

    def getAnsNum(self):
        return self.a

    def getValue(self):
        return self.value

    def getAnswer(self):
        answer = "False"
        if self.a == 1:
            answer = "True"
        return answer

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GAMEBOARD = 'gameboard'
QUESTION = 'question'
ANSWER = 'answer'


class Jeopardy:
    question_dict = {}
    board = []
    mode = GAMEBOARD
    curQ = None

    def __init__(self, screen, category_list):
        self.screen = screen

        # load fonts
        self.smallFont = pygame.font.Font(None, 48)
        self.bigFont = pygame.font.Font(None, 80)

        # load the questions
        #self.loadQuestions(questionFile)
        for i in range(len(category_list)):
            self.loadQuestions(category_list[i])

        # create gameboard
        self.board.append(list(self.question_dict.keys()))
        for p in range(100, 501, 100):
            self.board.append([p] * 6)

    '''def loadQuestions(self, filename):
        f = open(filename)
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(':')
            self.addQuestion(*data)'''

    '''def loadQuestions(self, category):
        global num_questions
        new_q_info_list = readQuestion(category)
        new_question_list = []
        for i in range(num_questions):
            new_question_info = new_q_info_list[i]
            if new_question_info[0] == 'MC':
                new_question = MCQuestion(new_question_info[1], new_question_info[2], new_question_info[3])
            elif new_question_info[0] == 'TF':
                new_question = TFQuestion(new_question_info[1], new_question_info[2])
            new_question_list.append(new_question)
        self.question_dict[category] = new_question_list'''

    def loadQuestions(self, category):
        global num_questions
        new_q_info_list = readQuestion(category)
        if category not in self.question_dict.keys():
            self.question_dict[category] = {}

        for i in range(num_questions):
            new_question_info = new_q_info_list[i]
            new_question_score = (i+1) * 100
            if new_question_info[0] == 'MC':
                new_question = MCQuestion(new_question_info[1], new_question_info[2], new_question_info[3], new_question_score)
            elif new_question_info[0] == 'TF':
                new_question = TFQuestion(new_question_info[1], new_question_info[2], new_question_score)
            self.question_dict[category][new_question_score] = new_question

    '''def addQuestion(self, category, points, q, a):
        if not category in self.qm.keys():
            self.qm[category] = {}
        self.qm[category][points] = Question(q, a)'''

    def mouseClick(self, pos):
        if self.mode == GAMEBOARD:
            print(pos[0])
            print(pos[1])
            
            # Do not run askQuestion() if clicking category         
            if pos[1] < 105: 
                pass
            # ask the appropriate question depending on the click position
            else:
                self.askQuestion(pos[0] / 133, pos[1] / 100)
                
        elif self.mode == ANSWER:
            self.mode = GAMEBOARD

    def answerKeyed(self, active_player, ans_num):
        if self.mode == QUESTION:
            correct_ans_num = self.curQ.getAnsNum()
            if ans_num == correct_ans_num:
                active_player.addPoints(self.curQ.getValue())
            self.mode = ANSWER

    def askQuestion(self, col, row):
        if row != 0:
            cat = self.board[0][int(col)]
            points = int(row) * 100
            if points != 0:
                self.curQ = self.question_dict[cat][points]
                self.board[int(row)][int(col)] = ''
                self.mode = QUESTION

    def drawTextCentered(self, str, skiperoo=-75):
        choperoo = len(str)

        font = self.smallFont

        # draw string and see if it is too long
        text = font.render(str, 1, WHITE)

        # if string is too long, choperoo!
        while text.get_rect().width > self.screen.get_rect().width:
            for c in range(int(choperoo / 2), choperoo):
                if str[c] == ' ':
                    choperoo = c
                    break
            # redraw string
            text = font.render(str[:choperoo], 1, WHITE)

        # find the centered rect for the drawing
        cr = text.get_rect()
        cr.center = self.screen.get_rect().center
        cr.y += skiperoo
        # draw
        self.screen.blit(text, cr)

        if choperoo != len(str):
            self.drawTextCentered(str[choperoo:], skiperoo + cr.height)

    def draw(self):
        if self.mode == GAMEBOARD:
            self.drawBoard()
        elif self.mode == QUESTION:
            self.drawTextCentered(str(self.curQ))
        elif self.mode == ANSWER:
            self.drawTextCentered(self.curQ.getAnswer())

    def drawBoard(self):
        xStart, xEnd = 0, 800
        yStart, yEnd = 0, 600
        xStep = xEnd // 6
        yStep = yEnd // 6

        # draw the grid

        print(xStep)
        for x in range(xStart, xEnd + 1, xStep):
            pygame.draw.line(self.screen, BLACK, (x, yStart), (x, yEnd), 5)
        for y in range(yStart, yEnd + 1, yStep):
            pygame.draw.line(self.screen, BLACK, (xStart, y), (xEnd, y), 5)

        # draw the labels
        for x in range(0, 6):
            text = self.smallFont.render(self.board[0][x], 1, WHITE)
            self.screen.blit(text, (x * xStep + 10, 25))
            for y in range(1, 6):
                text = self.bigFont.render(str(self.board[y][x]), 1, WHITE)
                self.screen.blit(text, (x * xStep + 7, y * yStep + 10))


def main():
    global category_list
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Jeopardy')
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 200))
    pygame.display.flip()
    # allsprites = pygame.sprite.renderPlain((fist, chimp))
    clock = pygame.time.Clock()

    # round 1
    jeopardy = Jeopardy(screen, category_list)
    player_one = Player('Testie Magee')

    # round 2
    #jeopardy = Jeopardy(screen, 'round2.txt', 2)

    answer_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]
    quit = False
    while not quit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                quit = True
            elif event.type == MOUSEBUTTONDOWN:
                jeopardy.mouseClick(pygame.mouse.get_pos())
            elif event.type == KEYDOWN and event.key in answer_keys:
                answer_index = int(event.key) - 48 - 1
                jeopardy.answerKeyed(player_one, answer_index)
        screen.blit(background, (0, 0))
        jeopardy.draw()
        pygame.display.flip()


if __name__ == '__main__':
    main()
