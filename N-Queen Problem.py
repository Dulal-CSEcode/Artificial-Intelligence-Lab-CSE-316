print("Enter the number of queens : ")
N = int(input())

# Creating an empty chessboard  as NxN matrix with all elements initialized 0
board = [[0]*N for _ in range(N)]

# Function for check if placing queen position (i,j) attack
def is_attack(i, j):
    # Checking for same column
    for k in range(0, i):
        if(board[k][j] == 1):
            return True

    # Checking upper right diagonal
    k = i - 1
    l = j + 1
    while (k >= 0 and l <= N - 1):
        if (board[k][l] == 1):
            return True
        k = k - 1
        l = l + 1

    # Checking upper left diagonal
    k = i - 1
    l = j - 1
    while (k >= 0 and l >= 0):
        if (board[k][l] == 1):
            return True
        k = k - 1
        l = l - 1

    return False

# Recursive function  place queens on board
def n_queen(row, n):
    if (n == 0):
        return True
    
    # Trying place queen in each column of current row
    for j in range(0, N):
        # If prossible place a queen this position
        if (not(is_attack(row, j))):
            board[row][j] = 1

            # Recursively trying to place the remaining queens
            if (n_queen(row + 1, n - 1)):
                return True

            # Backtracking if placing queen doesn't lead to a solution
            board[row][j] = 0

    # If nosafe position in this row, return False
    return False

#  function call to solve problem
n_queen(0, N)

# Printing final matrix representing placement of queens by 0
for i in board:
    print(i)