# Special Positions in a Binary Matrix
# Link - https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/

# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 
mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Approach1 - Brute force

def numSpecial(mat):
    n = len(mat)
    m = len(mat[0])
    
    ans = 0
    for row in range(n):
        for col in range(m):
            if mat[row][col] == 1:
                if sum(mat[row]) == 1:
                    sum_col = sum(mat[i][col] for i in range(n))
                    if sum_col == 1:
                        ans += 1
    return ans
    
mat = [[1,0,0],[0,0,1],[1,0,0]]
result = numSpecial(mat)
print(result)

# TC = 0(N*M) * 0(m+n)
# sc = 0(1)

# Approach2 - Better

def numSpecial(mat):
    n = len(mat)    # Number of rows
    m = len(mat[0]) # Number of columns
    
    # Step 1: Precompute row sums and column sums
    row_sums = [sum(mat[row]) for row in range(n)]
    col_sums = [sum(mat[row][col] for row in range(n)) for col in range(m)]
    
    ans = 0
    
    # Step 2: Check for special positions
    for row in range(n):
        for col in range(m):
            if mat[row][col] == 1:
                # Check if row_sums[row] == 1 and col_sums[col] == 1
                if row_sums[row] == 1 and col_sums[col] == 1:
                    ans += 1
    
    return ans

# Test case
mat = [[1,0,0],[0,0,1],[1,0,0]]
result = numSpecial(mat)
print(result)

# TC = 0(N*M)
# sc = 0(1)
