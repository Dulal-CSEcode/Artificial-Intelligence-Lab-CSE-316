#N-Queen Problem

print ("Enter the number of queens : ")
N = int(input())
#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

#current row i
def is_attack(i, j):
  # checking for column j
  for k in range(0, i):
    if(board[k][j] == 1):
      return True

  # checking upper right diagonal
  #check lower left diagonal
  k = i-1 #row
  l = j+1  #column
  while (k>=0 and l<=N-1):
    if (board[k][l] == 1):
      return True
    k=k-1
    l=l+1

  # checking upper left diagonal
  #upper left diagonal
  k = i-1
  l = j-1
  while (k>=0 and l>=0):
    if (board[k][l] == 1):
      return True
    k=k-1
    l=l-1

  return False

def n_queen(row, n):
  if (n==0):
    return True

  for j in range(0, N):
    if(not(is_attack(row, j))):
      board[row][j] = 1

      if (n_queen(row+1, n-1)):
        return True

      board[row][j] = 0 #backtracking
  return False

n_queen(0, N)

 #printing the matrix
for i in board:
    print(i)