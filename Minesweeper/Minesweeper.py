import pygame
from random import randint
pygame.init()


class Board:
    def __init__(self, board):
        self.board = board

    def __repr__(self):
        print_table(self.board)
        return "is your board"


class Square:
    def __init__(self, x, y, w, h, board, ij):
        self.rect = pygame.rect.Rect(x, y, w, h)
        i, j = ij
        self.x = x
        self.y = y
        self.visible = False
        self.flag = False


def game_setup(n, bombs):
    table = create_table(n)
    table = add_bombs(table, bombs)
    table = change_table(table)
    return table


def create_table(n):
    return [[0]*n for i in range(n)]


def add_bombs(table, bombs):
    for i in range(bombs):
        is_bomb = False
        while not is_bomb:
            x = randint(0, len(table) - 1)
            y = randint(0, len(table) - 1)
            if table[x][y] != 10:
                table[x][y] = 10
                is_bomb = True
    return table


def change_table(table):
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] == 10:
                table = update_downLeft(table, x, y)
                table = update_downMiddle(table, x, y)
                table = update_downRight(table, x, y)
                table = update_left(table, x, y)
                table = update_right(table, x, y)
                table = update_upLeft(table, x, y)
                table = update_upMiddle(table, x, y)
                table = update_upRight(table, x, y)
    return table

def update_downLeft(table, x, y):
    if x+1 < len(table[x]) and y-1 >= 0:
        if table[x+1][y-1] != 10:
            table[x+1][y-1] += 1
    return table


def update_downMiddle(table, x, y):
    if x+1 < len(table[0]):
        if table[x+1][y] != 10:
            table[x+1][y] += 1
    return table


def update_downRight(table, x, y):
    if x+1 < len(table[0]) and y+1 < len(table):
        if table[x+1][y+1] != 10:
            table[x+1][y+1] += 1
    return table


def update_left(table, x, y):
    if y-1 >= 0:
        if table[x][y-1] != 10:
            table[x][y-1] += 1
    return table


def update_right(table, x, y):
    if y+1 < len(table):
        if table[x][y+1] != 10:
            table[x][y+1] += 1
    return table


def update_upLeft(table, x, y):
    if x-1 >= 0 and y+1 < len(table):
        if table[x-1][y-1] != 10:
            table[x-1][y-1] += 1
    return table


def update_upMiddle(table, x, y):
    if x-1 >= 0:
        if table[x-1][y] != 10:
            table[x-1][y] += 1
    return table


def update_upRight(table, x, y):
    if x-1 >= 0 and y+1 < len(table):
        if table[x-1][y+1] != 10:
            table[x-1][y+1] += 1
    return table


def print_table(table):
    for i in table:
        print(i)


def restart_game(size, bombs):
    board = game_setup(size, bombs)
    print_table(board)

restart_game(8, 18)

