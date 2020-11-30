from random import randrange

def DisplayBoard(board):
    print("+-------+-------+-------+")
    for col in board:
        print("|\t|\t|\t|")
        print("|  ", end=" ")
        for fil in col:
            print(fil, "  |  ", end=" ")
        print("\n|\t|\t|\t|")
        print("+-------+-------+-------+")

def EnterMove(board):
    mov = input("Ingresa tu moviento: ")
    if int(mov) > 0 and int(mov) < 10:
        for col in range(len(board)):
            for fil in range(len(board[col])):
                if board[col][fil] == mov:
                    board[col][fil] = 'O'
                    return
    return

def VictoryFor(board, sign):
    if sign:
        sign = 'X'
    else:
        sign = 'O'
    ganarD1 = 0
    ganarD2 = 0

    for col in range(len(board)):
        ganarF = 0
        ganarC = 0
        for fil in range(len(board[col])):
            if board[col][fil] == sign:
                ganarF += 1
            if board[fil][col] == sign:
                ganarC += 1
        if ganarC == 3 or ganarF == 3:
            print("Gana", sign)
            return True
        if board[col][col] == sign:
            ganarD1 += 1
        if board[2-col][col] == sign:
            ganarD2 += 1
    
    if ganarD1 == 3 or ganarD2 == 3:
        print("Gana", sign)
        return True

    return False

def DrawMove(board):
    while True:
        mov = str(randrange(1,10))
        for col in range(len(board)):
            for fil in range(len(board[col])):
                if board[col][fil] == mov:
                    board[col][fil] = 'X'
                    DisplayBoard(board)
                    return
    return

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
DisplayBoard(board)
sign = True
while not VictoryFor(board, sign):
    sign = not sign
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board, sign):
        break
    sign = not sign
    DrawMove(board)