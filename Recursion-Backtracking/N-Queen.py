# N-Queens
# Link - https://leetcode.com/problems/n-queens/description/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

def solveNQueens(n):
    ans = []
    
    board = ["." * n for _ in range(n)]
    
    def is_safe(row, col, board, n):
        # Check for any queens in the three directions:

        for i in range(col):
            # Check left in the same row
            if board[row][i] == 'Q':
                return False
        
            # Check upper-left diagonal
            if row - (col - i) >= 0 and board[row - (col - i)][i] == 'Q':
                return False
        
            # Check lower-left diagonal
            if row + (col - i) < n and board[row + (col - i)][i] == 'Q':
                return False
    
        return True

    
    def helper(col,board,n):
        if col == n:
            ans.append(list(board))
            return 
        
        for row in range(n):
            if is_safe(row,col,board,n):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                helper(col+1, board,n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                
    helper(0,board,n)
    return ans
        

n = 4
result = solveNQueens(n)
print(result)