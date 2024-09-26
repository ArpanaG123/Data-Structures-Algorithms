# Find the Smallest Divisor Given a Threshold
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
# The test cases are generated so that there will be an answer.


# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).

# Link - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

# Brute force

import math

def smallestDivisor(arr,threshold):
    n = len(arr)
    mx = max(arr)
    
    for d in range(1,mx+1):
        sm = 0
        for i in range(n):
            sm += math.ceil(arr[i]/d)
            
        if sm <= threshold:
            return d
    return - 1
        

arr = [1,2,5,9]
threshold = 6
result = smallestDivisor(arr,threshold)
print(result)

# TC = 0(max(arr)*n)
# SC = 0(1)

# Optimsed code
import math

def sumByD(arr, div):
    n = len(arr)
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr,threshold):
    n = len(arr)
    mx = max(arr)
    
    n = len(arr)
    if n > threshold:
        return -1
    
    low = 1
    high = mx
    
    ans = -1
    
    while low <= high:
        mid = (low+high)//2
        
        if sumByD(arr,mid) <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
        

arr = [1,2,5,9]
threshold = 6
result = smallestDivisor(arr,threshold)
print(result)