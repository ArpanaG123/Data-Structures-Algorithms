#  Minimum Number of Days to Make m Bouquets

# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

# Link - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

# Brute force

def possible(arr,day,m,k):
    n = len(bloomday)
    cnt = 0
    noOfBqt = 0
    
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfBqt += cnt//k
            cnt = 0
    noOfBqt += cnt//k
    if noOfBqt >= m:
        return True
    else:
        return False
    
def minNumberOfDay(bloomday,m,k):
    
    n = len(bloomday)
    
    if n < m * k:
        return -1
        
    low = min(bloomday)
    high = max(bloomday)
    
    for i in range(low,high+1):
        if (possible(bloomday,i,m,k)):
            return i
    return -1

bloomday = [1,10,3,10,2]
m = 3
k = 1   
result = minNumberOfDay(bloomday,m,k)
print(result)

# TC = 0(min(arr) to max(arr) * n)
# SC = 0(1)

# Binary search

def possible(arr,day,m,k):
    n = len(bloomday)
    cnt = 0
    noOfBqt = 0
    
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfBqt += cnt//k
            cnt = 0
    noOfBqt += cnt//k
    if noOfBqt >= m:
        return True
    else:
        return False
    
def minNumberOfDay(bloomday,m,k):
    
    n = len(bloomday)
    
    if n < m * k:
        return -1
        
    low = min(bloomday)
    high = max(bloomday)
    
    ans = high
    
    while low <= high:
        mid = (low + high)//2
        
        if (possible(bloomday,mid,m,k)):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

bloomday = [1,10,3,10,2]
m = 3
k = 1   
result = minNumberOfDay(bloomday,m,k)
print(result)

# TC = 0(n * logn(max-min+1))
# SC = 0(1)