global n  
n = 4

def printBoard(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
            
    for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
            
    return True



def solveNQ(board, col):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solveNQ(board, col+1) == True:
                return True
            board[i][col] = 0
            
    return False


board = [ [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0] ] 

if solveNQ(board, 0) == False:
    print("solution Doesn't Exist") 

printBoard(board)