# Missing And Repeating
# Link - https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-missing-and-repeating

# Given an unsorted array arr of of positive integers. One number 'A' from set {1, 2,....,n} is missing and one number 'B' occurs twice in array. Find numbers A and B.
# Examples
# Input: 
arr = [2, 2]
# Output: 2 1
# Explanation: Repeating number is 2 and smallest positive missing number is 1.

# Brute force
arr = [4,3,6,2,1,1]

n = len(arr)

repeating = -1
missing = -1

for i in range(1,n+1):
    cnt = 0
    for j in range(0,n):
        if arr[j] == i:
            cnt += 1
    
    if cnt == 2:
        repeating = i
    if cnt == 0:
        missing = i
        

print([missing,repeating])

# TC = 0(N^2)
# SC = 0(1)

# Better - using hashing
arr = [4,3,6,2,1,1]

n = len(arr)

hashArr = [0]*(n+1)
repeating = -1
missing = -1

for i in range(n):
    hashArr[arr[i]] += 1
    
for i in range(1,n+1):
    if hashArr[i] == 2:
        repeating = i
    
    if hashArr[i] == 0:
        missing = i
        

print([missing,repeating])

# TC = 0(N)
# SC = 0(N)

# Optimal
a = [4,3,6,2,1,1]

def findMissingRepeatingNumbers(a):
    n = len(a)  # size of the array

    # Find Sn and S2n:
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6

    # Calculate S and S2:
    S, S2 = 0, 0
    for i in range(n):
        S += a[i]
        S2 += a[i] * a[i]

    # S-Sn = X-Y:
    val1 = S - SN

    # S2-S2n = X^2-Y^2:
    val2 = S2 - S2N

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2 // val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1 + val2) // 2
    y = x - val1

    return [x, y]

result = findMissingRepeatingNumbers(a)
print(result)

# TC = 0(N)
# SC = 0(1)

# Time Complexity and Space Complexity:
# Time Complexity: O(n), because we only loop through the array once to calculate the sum and sum of squares.
# Space Complexity: O(1), as no extra space is used apart from a few variables.


