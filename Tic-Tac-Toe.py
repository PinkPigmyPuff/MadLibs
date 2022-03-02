
# while an entire collum, row, or diagonal ISN'T filled with either all 'X' or 'Y', and the entire board isn't full
# ask p1 what square they would like to play in
# ask p2 what square they would like to play in
# win / lose

def tictactoe():
    board = ['N'] * 9
    while not gameover(board):
        pos1 = int(input("p1, which square would you like to play on (1 - 9)?")) - 1
        board[pos1] = 'X'
        print(board)
        pos2 = int(input("p2, which square would you like to play on (1 - 9)?")) - 1
        board[pos2] = 'Y'
        print(board)


def gameover(board):
    over = False
    lose = False
    if (board[0] and board[1] and board[2]) == 'X':
        over = True
    elif (board[0] and board[1] and board[2]) == 'Y':
        lose = True
    elif (board[1] and board[2] and board[3]) == 'X':
        over = True
    elif (board[1] and board[2] and board[3]) == 'Y':
        lose = True
    elif (board[2] and board[3] and board[4]) == 'X':
        over = True
    elif (board[2] and board[3] and board[4]) == 'Y':
        lose = True

    if lose:
        print("You lose")
        over = True
    return over


tictactoe()