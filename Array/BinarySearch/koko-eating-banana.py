# Koko Eating Bananas
# Link - https://leetcode.com/problems/koko-eating-bananas/description/

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

piles = [3,6,7,11]
h = 8
# Output: 4

# Explanation
# dry run
# 3/1
# 6/1
# 7/1
# 11/1,total exceeds the totalHours

# 3/2
# 6/2
# 7/2
# 11/2
# also exceeds the given totalHours

# 3/3
# 6/3
# 7/3
# 11/3
# also exceeds

# 3/4
# 6/4
# 7/4
# 11/4
# equal to given hours hence answer is 4

# Brute force

import math

piles = [3,6,7,11]
h = 8

def calculateTotalHours(piles, hourly):
    totalH = 0
    n = len(piles)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(piles[i] / hourly)
    return totalH

def minEatingSpeed(piles,h):
    n = len(piles)
    mx = max(piles)
    
    for i in range(1,mx+1):
        reqTime = calculateTotalHours(piles,i)
        
        if reqTime <= h:
            return i
          
ans = minEatingSpeed(piles, h)
print(ans)

# TC = 0(max(piles)*N)
# sc = 0(1)

# Optimised approach

import math

piles = [3,6,7,11]
h = 8

def totalHours(piles,speed):
    n = len(piles)
    
    totalH = 0
    for i in range(0,n):
        totalH += math.ceil(piles[i]/speed)
    
    return totalH

def minEatingSpeed(piles,h):

    mx = max(piles)
    
    low = 1
    high = mx
    
    ans = float('inf')
    
    while low < high:
        mid = (low+high)//2
        
        hours = totalHours(piles,mid)
        
        if hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
          
ans = minEatingSpeed(piles, h)
print(ans)

# TC = 0(N * logN)
