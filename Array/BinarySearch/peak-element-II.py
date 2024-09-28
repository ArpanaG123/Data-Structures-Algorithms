# Find a Peak Element II

# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
# you may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

# Link - https://leetcode.com/problems/find-a-peak-element-ii/description/

mat = [[1,4],[3,2]]
# Output: [0,1]
# Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

# optimal approach

def findMaxIndex(mat,n,m,col) -> int:
        idx = 0
        max_value = mat[0][col]

        for i in range(1,n):
            if mat[i][col] > max_value:
                max_value = mat[i][col]
                idx = i
        return idx

def findPeakGrid(mat) -> int:
    n = len(mat)
    m = len(mat[0])

    low = 0
    high = m-1

    while low <= high:
        mid = (low+high)//2

        maxRowIndx = findMaxIndex(mat,n,m,mid)

        # Checking neighbors
        left = mat[maxRowIndx][mid - 1] if mid - 1 >= 0 else -1
        right = mat[maxRowIndx][mid + 1] if mid + 1 < m else -1

        if mat[maxRowIndx][mid] > left and mat[maxRowIndx][mid] > right:
            return [mid,maxRowIndx]

        elif mat[maxRowIndx][mid] < left :
            high = mid - 1
        else:
            low = mid + 1

    return [-1,-1]

mat = [[1,4],[3,2]]
result = findPeakGrid(mat)
print(result)

