#  Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.

# Link - https://leetcode.com/problems/pascals-triangle/description/

numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Type1 = print element at mentioned row and mentioned column.
# eg = r - 5, c - 3 
# Output = 6

r = 5
c = 3

def ncr(R,C):
    res = 1
    for i in range(0,C):
        res = res * (R-i)
        res = res//(i+1)
    
    return res

def findElement(r,c):
    element = ncr(r-1,c-1)
    return element

result = findElement(r,c)
print(result)

# Type2 - print all element at nth row of pascals traingle

# eg. 
n = 5
# output = [1,4,6,4,1]

def ncr(R,C):
    res = 1
    for i in range(0,C):
        res = res * (R-i)
        res = res//(i+1)
    
    return res

def printElement(n):
    result = []

    for i in range(1,n+1):
        ans = ncr(n-1,i-1)
        result.append(ans)
    return result
    
n = 5
output = printElement(n)
print(output)


# Type3 - generate pascals triangle

numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def ncr(R,C):
    res = 1
    for i in range(0,C):
        res = res * (R-i)
        res = res//(i+1)
    
    return res

def pasaclTriangle(n):
    ans = []

    for row in range(1,n+1):
        tempList = []
        for col in range(1,row+1):
            tempList.append(ncr(row-1,col-1))
        ans.append(tempList)
    return ans
    
n = 5
output = pasaclTriangle(n)
print(output)

# Optimal

def generatePascal(row):
    ans = 1
    ansRow = [1]
    for col in range(1,row):
        ans = ans * (row-col)
        ans = ans//col
        ansRow.append(ans)
    
    return ansRow

def pascalTriangle(n):
    ans = []

    for row in range(1,n+1):
        tempList = []
        ans.append(generatePascal(row))
        
    return ans
    
n = 5
output = pascalTriangle(n)
print(output)

# Topic - array and DP
