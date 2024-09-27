# Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

# Link - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# Brute force
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def daysReq(weights,cap):
    n = len(weights)
    day = 1
    load = 0
    
    for i in range(n):
        if load + weights[i] > cap:
            day = day + 1
            load = weights[i]
        else:
            load += weights[i]
            
    return day
    
def shipWithinDays(weights,days):
    mx = max(weights)
    sm = sum(weights)
    
    for d in range(mx,sm+1):
        reqDays = daysReq(weights, d)
        
        if reqDays <= days:  # If the days required are within the limit
            return d
            
res = shipWithinDays(weights,days)
print(res)

# TC = 0(max(arr)-sum(arr))*0(n)
# SC = 0(1)

# Optimal
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def daysReq(weights,cap):
    n = len(weights)
    day = 1
    load = 0
    
    for i in range(n):
        if load + weights[i] > cap:
            day = day + 1
            load = weights[i]
        else:
            load += weights[i]
            
    return day
    
def shipWithinDays(weights,days):

    mx = max(weights)
    sm = sum(weights)
    
    low = mx
    high = sm
    
    ans = low
    
    while low <= high:
        mid = (low+high)//2
        
        if daysReq(weights,mid) <= days:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
            
res = shipWithinDays(weights,days)
print(res)

# TC = 0(N) * 0(logn(max(arr))-sum(arr))
# SC = 0(1)