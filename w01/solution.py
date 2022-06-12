'''
Tic-Tac-Toe: A Solution
Author: Hikaru Imaizumi

'''

def main():
    board = newBoard()
    printTheBoard(board)

    ans = int(input("x's turn to choose a square (1-9):"))
    updatedBoard = editBoard(ans, board)
    printTheBoard(updatedBoard)

def newBoard():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def editBoard(ans, board):
    for i in range(9):
        if ans == i+1:
            board[i] = "x"
            return board
    return "Try again"

def printTheBoard(board):
    printBoard = f"{board[0]} | {board[1]} | {board[2]} \n- + - + -\n{board[3]} | {board[4]} | {board[5]} \n- + - + -\n{board[6]} | {board[7]} | {board[8]}"
    print(printBoard)

if __name__ == "__main__":
    main()