b = [[1,0,1,0,0,0,0,6,5],
     [0,0,0,6,0,9,0,8,0],
     [3,0,0,0,4,8,0,0,0],
     [0,0,0,0,2,0,0,5,8],
     [0,0,6,0,0,0,1,2,0],
     [0,0,0,0,9,0,0,0,0],
     [0,4,0,0,0,0,0,0,0],
     [0,0,0,3,0,0,5,7,0],
     [5,2,3,1,0,0,4,0,0]]

a = [[4,8,1,2,7,3,9,6,5],
     [7,5,2,6,1,9,3,8,4],
     [3,6,9,5,4,8,2,1,7],
     [9,3,4,7,2,1,6,5,8],
     [8,7,6,4,3,5,1,2,9],
     [2,1,5,8,9,6,7,4,3],
     [6,4,7,9,5,2,8,3,1],
     [1,9,8,3,6,4,5,7,2],
     [5,2,3,1,8,7,4,9,6]]

# Prints the sudoku board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Gets the coordinates of an empty square in the sudoku board
def getEmptySquare(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None

# Checks if inserted number is valid
def validNumber(board, num, position):
    # Check row
    for i in range(len(board)):
        # If the square equals the number and it isn't the position itself
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        # If the square equals the number and it isn't the position itself
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check box
    boxRow = position[0] // 3
    boxColumn = position[1] // 3

    for i in range(boxRow * 3, boxRow * 3 + 3):
        for j in range(boxColumn * 3, boxColumn * 3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True

def solve(board):
    square = getEmptySquare(board)
    # Base Case
    if square is None:
        return True
    else:
        row, column = square

    # Recursive case
    for i in range(1, 10):
        if validNumber(board, i , (row, column)):
            board[row][column] = i
            # If i of that branch solved it
            if solve(board):
                return True
            # Will not get to here if branch is correct
            # If the board is not solved on that branch, sets back to 0 and tries next i
            board[row][column] = 0
    
    return False

printBoard(b)
print("# # # # # # # # # # #")

if not solve(b):
    print("Invalid Board")
else:
    printBoard(b)