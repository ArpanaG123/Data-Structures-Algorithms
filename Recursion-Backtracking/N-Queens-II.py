# N-Queens II
# Link - https://leetcode.com/problems/n-queens-ii/description/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

def totalNQueens(n):
    ans = []
    board = ["." * n for _ in range(n)]
    
    def is_safe(board,row,col,n):
        for i in range(col):
            if board[row][i] == "Q":
                return False
            
            if row - (col-i) >= 0 and board[row-(col-i)][i] == "Q":
                return False
            
            if row + (col-i) < n and board[row + (col-i)][i] == "Q":
                return False
        return True
        
    def helper(col,board):
        if col == n:
            ans.append(list(board))
            return 
        
        for row in range(n):
            if is_safe(board,row,col,n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                helper(col+1,board)
                board[row] = board[row][:col] + "." + board[row][col+1:]
    
    helper(0,board)
    return len(ans)
    
n = 4
result = totalNQueens(n)
print(result)
# output = 2