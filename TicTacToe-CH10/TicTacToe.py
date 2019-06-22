# invent your game with pytho 4th edition
import random


# This function prints out the board that it was passed.
# "board" is a list of 10 strings representing the board (ignoreindex).
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Lets the player type which letter they want to be.
# Returns a list with the player's letter as the first item and the computer 's letter as the second.
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do You Want be X or O')
        letter = input().upper()
    # The first element in the list is the player's letter; the second isthe computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# Randomly choose which player goes first.
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


# Given a board and a player's letter, this function returns True if that player has won.
# We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # Down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # Down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # Down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # Diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # Diagonal


# Make a copy of the board list and return it.
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


# Return True if the passed move is free on the passed board.
def isSpaceFree(board, move):
    return board[move] == ' '


# Let the player enter their move.
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What's your next move(1-9)")
        move = input()
    return int(move)


# Returns a valid move from the passed list on the passed board.
# Returns None if there is no valid move.
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# Given a board and the computer 's letter, determine where to move and return that move.
def getComputerMove(board, compLetter):
    if compLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, compLetter, i)
            if isWinner(boardCopy, compLetter):
                return i

        # check if the player will win in the next move and block him
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # try to take one of the corners if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # try to take the center if it's free
    if isSpaceFree(board, 5):
        return 5

    # move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# Return True if every space on the board has been taken. Otherwise, return False.
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Welcome to Tic-Tac-Toe")
while True:
    # reset the board
    theBoard = [' '] * 10
    playerLetter, compLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The " + turn + " will go first")
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("HOOOOORY! you won the game")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game in a tie")
                    break
                else:
                    turn = "computer"
        else:
            # computer's turn
            move = getComputerMove(theBoard, compLetter)
            makeMove(theBoard, compLetter, move)
            if isWinner(theBoard, compLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game in a tie")
                    break
                else:
                    turn = 'player'
    print("Do you want to play again(yes or no)")
    if not input().lower().startswith('y'):
        break
