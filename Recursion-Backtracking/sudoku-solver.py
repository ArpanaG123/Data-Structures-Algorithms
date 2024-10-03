# Sudoku Solver
# Link - https://leetcode.com/problems/sudoku-solver/description/

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

def solveSudoku(board):
    def isValid(board, row, col, c):
        # Check the row and column
        for i in range(9):
            if board[i][col] == c:  # check column
                return False
            if board[row][i] == c:  # check row
                return False
            # Check the 3x3 sub-grid
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def helper(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":  # Empty cell
                    for c in "123456789":  # Try digits 1-9
                        if isValid(board, i, j, c):
                            board[i][j] = c  # Place digit
                            if helper(board):  # Recursively solve the rest
                                return True
                            else:
                                board[i][j] = "."  # Backtrack if not solvable
                    return False  # No valid digit was found
        return True  # Board is completely solved

    helper(board)  # Call the helper to solve the board
    return board  # Return the solved board

# Sudoku puzzle
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

# Solve the Sudoku puzzle
result = solveSudoku(board)
print(result)