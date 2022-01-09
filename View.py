import sys
import math
import time

import pygame as pygame

from Maze import Maze

class View:

    def __int__(self):
        pygame.init()
        self.start = 0
        self.end = 0

    #Draws the gird
    def drawGrid(self, size, screen, screenSize, blockSize):
        for x in range(0, screenSize, blockSize):
            for y in range(0, screenSize, blockSize):
                rect = pygame.Rect(x,y,blockSize, blockSize)
                pygame.draw.rect(screen, (0,0,0), rect, 1)

    #Sets up the GUI and some variables
    def setUpScreen(self, size, screen):
        lightPurple = pygame.Color("#C7CEEA")
        pygame.init()
        screen.fill(lightPurple)
        blocks = []
        count = 0
        return screen, blocks, count

    #The main "engine" of the gui class, running the while loop, screen updates and events
    def runGame(self, maze, size):
        #Setting up background and screen
        blockSize, screenSize, screen = self.accountForOddSize(size)
        screen, blocks, count = self.setUpScreen(size, screen)
        while True:
            pygame.font.init()
            self.drawGrid(size, screen, screenSize, blockSize)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #At count == 2 users are able to drag mouse and click to select multiple blocks
                if event.type == pygame.MOUSEMOTION and count == 2:
                    self.runMouseMotionEvent(size, blockSize, blocks, screen)
                #Listening for first two mouse events (start and end position)
                if event.type == pygame.MOUSEBUTTONDOWN and count < 2:
                    self.runMouseClickInEvent(blockSize,screen,count)
                    count += 1
                #Press up arrow to solve maze
                if event.type == pygame.KEYUP:
                    self.runKeyUpEvent(screen, maze, self.start, self.end, blocks, blockSize)
            pygame.display.update()

    #Runs BFS algoritm and transfers answer to GUI
    def runKeyUpEvent(self, screen, maze, start, end, blocks, blockSize):
            #Runs BFS to find shortest route
            shortest = maze.run(self.start, self.end, blocks)
            for cord in shortest[1:-1]:
                x = cord[0] * blockSize
                y = cord[1] * blockSize
                color = pygame.Color("#FFDAC1")
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, color, rect)

    #Handles mouse click ins when count is less than 2, (Selecting start position and end position)
    def runMouseClickInEvent(self, blockSize,screen,count):

        pos = pygame.mouse.get_pos()
        point = [pos[1] // blockSize, pos[0] // blockSize]
        # Turning screen position into matric codinates
        x, y = self.makeCordinates(pos[0], pos[1], blockSize)
        # Selecting starting position, changing block color
        if count == 0:
            rect = pygame.Rect(x, y, blockSize, blockSize)
            self.start = [point[1], point[0]]  # Setting start position codinates
            lightGreen = pygame.Color("#B5EAD7")
            pygame.draw.rect(screen, lightGreen, rect)
            count += 1
        # Selecting end postion, changing block color
        elif count == 1:
            rect = pygame.Rect(x, y, blockSize, blockSize)
            self.end = [point[1], point[0]]  # Setting end position codinates
            lightRed = pygame.Color("#FF9AA2")
            pygame.draw.rect(screen, lightRed, rect)
            count += 1

    #Runs a while loop to allow users to select blocked blocks by clicking and dragging mouse
    def runMouseMotionEvent(self, size, blockSize, blocks, screen):
        stillPressed = pygame.mouse.get_pressed(3)[0]
        while stillPressed:
            pos = pygame.mouse.get_pos()
            point = [pos[1] // blockSize, pos[0] // blockSize]
            x,y = self.makeCordinates(pos[0],pos[1],blockSize)
            rect = pygame.Rect(x, y, blockSize, blockSize)
            blocks.append([point[1], point[0]])
            pygame.draw.rect(screen, (0, 0, 0), rect)
            break

    #Turn screen position to cordinates
    def makeCordinates(self, num1, num2, blockSize):
        x = (num1// blockSize) * blockSize
        y = (num2 // blockSize) * blockSize
        return x,y

    #Changes proper values if matrix size is input to be odd
    def accountForOddSize(self,size):
        screenSize = 800
        blockSize = screenSize // size
        screen = pygame.display.set_mode((800, 800))
        # Adjusting screen for odd sizes
        if size % 2 == 1:
            leftOver = (800 % size) * size
            screenSize = leftOver * size
            blockSize = (screenSize) // size
            screen = pygame.display.set_mode((screenSize, screenSize))
        return blockSize, screenSize, screen
