# Row With Maximum Ones
# Link - https://leetcode.com/problems/row-with-maximum-ones/description/
# Link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
# Return an array containing the index of the row, and the number of ones in it.

 
mat = [[0,1],[1,0]]
# Output: [0,1]
# Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1]. 

# Brute force

def rowAndMaximumOnes(mat):
    n = len(mat)
    m = len(mat[0])
    
    count_max = 0
    idx = -1
    
    for i in range(n):
        cnt_ones = sum(mat[i])
        if cnt_ones > count_max:
            count_max = cnt_ones
            idx = i
    
    return [idx,count_max]
        

mat = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
result = rowAndMaximumOnes(mat)
print(result)

# Time Complexity: O(n X m), where n = given row number, m = given column number.
# Reason: We are using nested loops running for n and m times respectively.
# sc = 0(1)

# Optimal

def lowerBound(arr,n,x):
    low = 0
    high = n-1
    ans = n
    
    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
    
def rowAndMaximumOnes(mat):
    
    n = len(mat)
    m = len(mat[0])
    count_max = float('-inf')
    idx = -1
    
    for i in range(n):
        first_ones = lowerBound(mat[i],m,1)
        cnt_ones = m - first_ones
        if cnt_ones > count_max:
            count_max = cnt_ones
            idx = i
    
    return [idx,count_max]
        

mat = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
result = rowAndMaximumOnes(mat)
print(result)
# TC = O(n * log m)

# Approach3
def rowAndMaximumOnes(mat):
    
    n = len(mat)
    m = len(mat[0])
    count_max = 0
    idx = 0
    
    for i in range(n):
        cnt_ones = mat[i].count(1)
        if cnt_ones > count_max:
            count_max = cnt_ones
            idx = i
    
    return [idx,count_max]
        

mat = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
result = rowAndMaximumOnes(mat)
print(result)
# TC = O(n * m)
