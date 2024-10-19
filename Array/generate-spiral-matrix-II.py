# Spiral Matrix II
# Link - https://leetcode.com/problems/spiral-matrix-ii/description/

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

def generateMatrix(n):

    mat = [[0] * n for _ in range(n)]
    top = 0
    left = 0
    right = n-1
    bottom = n-1
    val = 1

    while left <= right and top <= bottom:
        for i in range(left,right+1):
            mat[top][i] = val
            val += 1
        top += 1

        for i in range(top,bottom+1):
            mat[i][right] = val
            val += 1
        right -= 1

        if top <= bottom:
            for i in range(right,left-1,-1):
                mat[bottom][i] = val
                val += 1
            bottom -= 1
            
        if left <= right:
            for i in range(bottom,top-1,-1):
                mat[i][left] = val
                val += 1
            left += 1
    return mat

result = generateMatrix(n)
print(result)