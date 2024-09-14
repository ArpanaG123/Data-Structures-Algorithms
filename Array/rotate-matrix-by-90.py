# Rotate Image
# Link - https://leetcode.com/problems/rotate-image/description/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Brute force
mat = [[1,2,3],[4,5,6],[7,8,9]]

n = len(mat)
m = len(mat[0])

ans = [[0]* n for _ in range(n)]

for i in range(0,n):
    for j in range(0,m):
        ans[j][n-i-1] = mat[i][j]
print(ans)

# TC = 0(N^2)
# SC = 0(N)


# Method - optimal approach

mat = [[1,2,3],[4,5,6],[7,8,9]]

n = len(mat)
m = len(mat[0])

# 0(n/2) + 0(n/2)
for i in range(0,n):
    for j in range(i+1,m):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# 0(n)*n/2(for reverse)
for i in range(0,n):
    mat[i].reverse()
print(mat)

# TC = 0(N) + 0(n*n/2)
# SC = 0(1)