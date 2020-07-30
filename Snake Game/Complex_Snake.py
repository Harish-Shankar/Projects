import math
import random
import pygame
import tkinter as tk
from  tkinter import messagebox

class cube(object):
    rows = 0
    width = 0
    def __init__(self, start, directionX=1, directionY=0, color=(255, 0, 0)):
        pass

    def move(self, directionX, directionY):
        pass

    def draw(self, window, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, position):
        self.color = color
        self.head = cube(position)
        self.body.append(self.head)
        self.directionX = 0
        self.directionY = 1

    def move(self):
        pass

    def reset(self, position):
        pass

    def add_cube(self):
        pass

    def draw(self, window):
        pass

def drawGrid(width, rows, window):
    size = width//rows
    x = 0
    y = 0

    for i in range(rows):
        x+=size
        y+=size

        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))

def redrawWindow(width, rows, window):
    window.fill((0, 0, 0))
    drawGrid(width, rows, window)
    pygame.display.update()

def snackGenerator(rows, items):
    pass

def messageBox(subject, content):
    pass

def main():
    width = 500
    height = 500
    rows = 20
    window = pygame.display.set_mode((width, height))
    snake_player = snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()

    while (flag):
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(width, rows, window)


main()
