# Spiral Matrix
# Link - https://leetcode.com/problems/spiral-matrix/description/

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


# Efficient and cleaner code
mat = [[1,2,3],[4,5,6],[7,8,9]]

n = len(mat)
m = len(mat[0])
top = 0
left = 0
right = m-1
bottom = n-1

ans = []

while left <= right and top <= bottom:
    for i in range(left,right+1):
        ans.append(mat[top][i])
    top += 1
    
    for i in range(top,bottom+1):
        ans.append(mat[i][right])
    right -= 1
    
    if top <= bottom:
        for i in range(right,left-1,-1):
            ans.append(mat[bottom][i])
        bottom -= 1
        
    if left <= right:
        for i in range(bottom,top-1,-1):
            ans.append(mat[i][left])
        left += 1

print(ans)

# TC = 0(N*M)
# SC = 0(N*M)