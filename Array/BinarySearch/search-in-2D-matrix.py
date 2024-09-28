# Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Link - https://leetcode.com/problems/search-a-2d-matrix/description/


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# Output: true

# Brute force

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

def searchIn2DMatrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(0,n):
        for j in range(0,m):
            if matrix[i][j] == target:
                return True
    
    return False
    
res = searchIn2DMatrix(matrix,target)
print(res)

# TC = 0(N*M)
# SC = 0(1)

# Better

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

def binarySearch(arr,target):
    n = len(arr)
    
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

def searchIn2DMatrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(0,n):
        if matrix[i][0] <= target <= matrix[i][m-1]:
            return binarySearch(matrix[i],target)
    return False
    
res = searchIn2DMatrix(matrix,target)
print(res)

# TC = 0(N) + 0(logm)
# SC = 0(1)

# Optimal

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5

def searchIn2DMatrix(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    
    low = 0
    high = n*m - 1
    
    while low <= high:
        mid = (low + high)//2
        
        row = mid//m
        col = mid%m
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False
    
res = searchIn2DMatrix(matrix,target)
print(res)

# TC = 0(log n*m)
# SC = 0(1)