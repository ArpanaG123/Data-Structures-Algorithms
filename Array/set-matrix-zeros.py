# Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Link - https://leetcode.com/problems/set-matrix-zeroes/description/

matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Brute force
mat = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
n = len(mat)
m = len(mat[0])

def markRow(i):
    for j in range(0,m):
        if mat[i][j] != 0:
            mat[i][j] = -1
            
def markCol(j):
    for i in range(0,n):
        if mat[i][j] != 0:
            mat[i][j] = -1

print("Original Matrix:",mat)

for i in range(0,n):
    for j in range(0,m):
        if mat[i][j] == 0:
            markRow(i)
            markCol(j)
            
print("Matrix after marking with -1:",mat)

for i in range(0,n):
    for j in range(0,m):
        if mat[i][j] == -1:
            mat[i][j] = 0

print("Final matrix after set zeroes:",mat)

# TC = 0(N*M) + 0(N*M) + 0(N) + 0(M) = 0(N^3 * M ^3)
# SC = 0(1)

# Better Approach

mat = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
n = len(mat)
m = len(mat[0])

col = [0]*m
row = [0]*n

for i in range(0,n):
    for j in range(0,m):
        if mat[i][j] == 0:
            row[i] = 1
            col[j] = 1
print(col)
print(row)

for i in range(0,n):
    for j in range(0,m):
        if row[i] or col[j]:
            mat[i][j] = 0
print("fianl matrix is after setting zeros:",mat)

# TC = 0(N*M) + 0(N*M) = 0(2*(N*M))
# SC = 0(N) + 0(M)

# Optimal approach

def zeroMatrix(matrix, n, m):
    # int row[n] = {0}; --> matrix[..][0]
    # int col[m] = {0}; --> matrix[0][..]

    col0 = 1
    # step 1: Traverse the matrix and
    # mark 1st row & col accordingly:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark i-th row:
                matrix[i][0] = 0

                # mark j-th column:
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                # check for col & row:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    #step 3: Finally mark the 1st col & then 1st row:
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix



matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
ans = zeroMatrix(matrix, n, m)
print(ans)

# TC = 0(N*M)
# SC = 0(1)


# Approach:---

# The steps are as follows:
# First, we will traverse the matrix and mark the proper cells of 1st row and 1st column with 0 accordingly. The marking will be like this: if cell(i, j) contains 0, we will mark the i-th row i.e. matrix[i][0] with 0 and we will mark j-th column i.e. matrix[0][j] with 0.
# If i is 0, we will mark matrix[0][0] with 0 but if j is 0, we will mark the col0 variable with 0 instead of marking matrix[0][0] again.
# After step 1 is completed, we will modify the cells from (1,1) to (n-1, m-1) using the values from the 1st row, 1st column, and col0 variable.
# We will not modify the 1st row and 1st column of the matrix here as the modification of the rest of the matrix(i.e. From (1,1) to (n-1, m-1)) is dependent on that row and column.
# Finally, we will change the 1st row and column using the values from matrix[0][0] and col0 variable. Here also we will change the row first and then the column.
# If matrix[0][0] = 0, we will change all the elements from the cell (0,1) to (0, m-1), to 0.
# If col0 = 0, we will change all the elements from the cell (0,0) to (n-1, 0), to 0.
# Now, in the second step we will try to start modifying the cells with value 0 from (0,0). First, we will change the value of (0,0) to 0 as col0 is marked with 0. After that, while checking for cell (0, 3) we will find that the value of (0,0) is 0. And we will again modify the cell (0,3) with 0. But this should not happen as (0,0) was initially 1 and that is why (0,3) should remain with the value 1.
# This is why we cannot change the 1st row and 1st column on the first go as the rest of the matrix is dependent on them. If we do it, the modification of the matrix will be incorrect.
# In the 3rd step, why we are marking the 1st row first and then the 1st column:
# We can notice that the modification of the 1st row is dependent on matrix[0][0] and the modification of the 1st column is dependent on col0 which is an independent variable. Now, if we modify the 1st column first, matrix[0][0] might be changed and this will hinder the modification of the 1st row as well. But if we simply do the opposite, the 1st row will be changed first, based on the value matrix[0][0] and then the 1st column will be changed based on the variable col0. This is why the order of change matters.

