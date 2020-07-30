import random
board = [' ' for x in range(10)]

def insertLetter(letter, move):
    board[move]=letter

def spaceChecker(move):
    return(board[move]==' ')

def winner(board, letter):
    return(board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)

def playerMove():
    check = True
    while(check):
        move = input("Please enter a position to place \'X\' (1-9)")
        try:
            move = int(move)
            if(move>0 and move<10):
                if(spaceChecker(move)):
                    check = False
                    insertLetter('X', move)
                else:
                    print("The space is occupied")
            else:
                print("Please enter a valid position")
        except:
            print("Please enter a number")

def compMove():
    possible = [i for i, letter in enumerate(board) if letter == ' ' and i != 0]
    move = 0

    for j in ['O', 'X']:
        for k in possible:
            board_copy = board[:]
            board_copy[k] = j
            if(winner(board_copy, j)):
                move = k
                return move

    corners = []
    for i in possible:
        if(i in [1,3,7,9]):
            corners.append(i)
    if(len(corners)>0):
        move = randomMove(corners)
        return(move)

    if(5 in possible):
        move = 5
        return move

    edges = []
    for i in possible:
        if (i in [2, 4, 6, 8]):
            edges.append(i)
    if (len(corners) > 0):
        move = randomMove(edges)

    return (move)

def randomMove(l):
    return(l[random.randrange(0, len(l))])

def boardFull(board):
    if(board.count(' ')>1):
        return(False)
    else:
        return(True)

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def main():
    while not(boardFull(board)):
        if not(winner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("O\'s won")
            break
        if not(winner(board, 'X')):
            move = compMove()
            if(move==0):
                break
            else:
                insertLetter('O', move)
                print("Coputer place an \'O\' in position", move)
                printBoard(board)
        else:
            print("X\'s won")
            break

    if(boardFull(board)):
        print("Tie")

while (True):
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
