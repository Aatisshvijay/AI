# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col, n):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on the right side
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Recursive function to solve the N-Queens problem
def solve_n_queens(board, row, n):
    # Base case: If all queens are placed, print the solution
    if row == n:
        print_board(board, n)
        print()
        return True

    # Try placing a queen in each column of the current row
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            # Recur to place the rest of the queens
            res = solve_n_queens(board, row + 1, n) or res
            # Backtrack and remove the queen
            board[row][col] = 0

    return res

# Function to print the chessboard
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# Main function
def eight_queens():
    n = 8  # Size of the chessboard (8x8 for 8 queens problem)
    board = [[0 for _ in range(n)] for _ in range(n)]

    print("\n--- Solutions to the 8 Queens Problem ---\n")
    if not solve_n_queens(board, 0, n):
        print("No solutions exist.")

# Run the 8 Queens Problem Solver
eight_queens()
