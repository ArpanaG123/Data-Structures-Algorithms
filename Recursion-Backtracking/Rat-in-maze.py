# Rat in a Maze Problem - I
# Link - https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

# Consider a rat placed at (0, 0) in a square matrix mat of order n* n. It has to reach the destination at (n - 1, n - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell. In case of no path, return an empty list. The driver will output "-1" automatically.

# Input: mat[][] = [[1, 0, 0, 0],
#                 [1, 1, 0, 1], 
#                 [1, 1, 0, 0],
#                 [0, 1, 1, 1]]
# Output: DDRDRR DRDDRR
# Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.


def findPath(m):
    # code here
    res = []
    row = len(m)
    col = len(m[0])
        
    def backtrack(m,res,row,col,i,j,s):
        if i == row-1 and j == col-1 and m[i][j] == 1:
            res.append(s)
            return
                
        if i < 0 or j < 0 or i >= row or j >= col or m[i][j] == 0:
            return 
            
        m[i][j] = 0
            
        # Move down
        backtrack(m, res, row,col, i + 1, j, s + 'D')
        # Move up
        backtrack(m, res, row,col, i - 1, j, s + 'U')
        # Move right
        backtrack(m, res, row,col, i, j + 1, s + 'R')
            # Move left
        backtrack(m, res, row,col, i, j - 1, s + 'L')
            
        # Unmark the cell (backtrack)
        m[i][j] = 1
            
    if m[0][0] == 1:
        backtrack(m, res, row,col, 0, 0, "")
        
    return res

m = [      
    [1, 0, 0, 0],
    [1, 1, 0, 1], 
    [1, 1, 0, 0],
    [0, 1, 1, 1]
    ]
result = findPath(m)
print(result)

# Output: DDRDRR DRDDRR
        
