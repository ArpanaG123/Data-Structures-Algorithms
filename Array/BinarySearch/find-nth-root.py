# Find Nth root of M
# You are given 2 numbers (n , m); the task is to find n√m (nth root of m).

# Link - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-nth-root-of-m
 

# Input: n = 2, m = 9
# Output: 3
# Explanation: 32 = 9

def findNthRoot(n, m):
    low = 1
    high = m
    
    
    while low <= high:
        mid = (low + high) // 2
        mid_power_n = mid ** n  # Calculate mid raised to the power of n
        
        if mid_power_n == m:  # If mid^n is exactly m, return mid
            return mid
        elif mid_power_n > m:  # If mid^n is greater than m, reduce the high bound
            high = mid - 1
        else:  # If mid^n is less than m, increase the low bound
            low = mid + 1
    
    return -1  # Return the floor of the nth root

n = 4
m = 69
result = findNthRoot(n,m)
print(result)
