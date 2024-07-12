print("Enter the number of queens: ")
N = int(input())

# Creating an empty chessboard as an NxN matrix with all elements initialized to 0
board = [[0]*N for _ in range(N)]

# List to store all valid configurations
solutions = []

# Function to check if placing queen position (i,j) is under attack
def is_attack(i, j):
    # Checking for the same column
    for k in range(0, i):
        if board[k][j] == 1:
            return True

    # Checking upper right diagonal
    k = i - 1
    l = j + 1
    while k >= 0 and l <= N - 1:
        if board[k][l] == 1:
            return True
        k -= 1
        l += 1

    # Checking upper left diagonal
    k = i - 1
    l = j - 1
    while k >= 0 and l >= 0:
        if board[k][l] == 1:
            return True
        k -= 1
        l -= 1

    return False

# Recursive function to place queens on the board
def n_queen(row, n):
    if n == 0:
        solutions.append([row[:] for row in board])
        return

    # Trying to place a queen in each column of the current row
    for j in range(0, N):
        # If it's possible to place a queen in this position
        if not is_attack(row, j):
            board[row][j] = 1

            # Recursively trying to place the remaining queens
            n_queen(row + 1, n - 1)

            # Backtracking if placing the queen doesn't lead to a solution
            board[row][j] = 0

# Function call to solve the problem
n_queen(0, N)

# Printing all valid configurations
for solution in solutions:
    for row in solution:
        print(row)
    print()
