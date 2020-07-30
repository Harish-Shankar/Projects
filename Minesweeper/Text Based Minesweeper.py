from random import randint
from math import floor


def board_setup(n, bombs):
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
            if table[x][y] != 9:
                table[x][y] = 9
                is_bomb = True
    return table


def change_table(table):
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] == 9:
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
        if table[x+1][y-1] != 9:
            table[x+1][y-1] += 1
    return table


def update_downMiddle(table, x, y):
    if x+1 < len(table[0]):
        if table[x+1][y] != 9:
            table[x+1][y] += 1
    return table


def update_downRight(table, x, y):
    if x+1 < len(table[0]) and y+1 < len(table):
        if table[x+1][y+1] != 9:
            table[x+1][y+1] += 1
    return table


def update_left(table, x, y):
    if y-1 >= 0:
        if table[x][y-1] != 9:
            table[x][y-1] += 1
    return table


def update_right(table, x, y):
    if y+1 < len(table):
        if table[x][y+1] != 9:
            table[x][y+1] += 1
    return table


def update_upLeft(table, x, y):
    if x-1 >= 0 and y+1 < len(table):
        if table[x-1][y-1] != 9:
            table[x-1][y-1] += 1
    return table


def update_upMiddle(table, x, y):
    if x-1 >= 0:
        if table[x-1][y] != 9:
            table[x-1][y] += 1
    return table


def update_upRight(table, x, y):
    if x-1 >= 0 and y+1 < len(table):
        if table[x-1][y+1] != 9:
            table[x-1][y+1] += 1
    return table


def print_board(table):
    for i in table:
        print(i)


def main():
    rows = int(input("How many rows do you want in the board"))
    game_end = False
    bombs = floor((rows**2)*(1/3))
    shown_board = [['X']*rows for i in range(rows)]
    bomb_board = board_setup(rows, bombs)
    print_board(shown_board)
    print_board(bomb_board)

main()
