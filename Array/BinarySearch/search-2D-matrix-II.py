# Search a 2D Matrix II

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Link - https://leetcode.com/problems/search-a-2d-matrix-ii/description/


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
# Output: true

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 26

def searchMatrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    
    i = 0
    j = m-1
    
    while i < n and j >= 0:
        curr = matrix[i][j]
        
        if curr == target:
            return True
        elif curr > target:
            j -= 1
        else:
            i += 1
    
    return False
    
res = searchMatrix(matrix,target)
print(res)