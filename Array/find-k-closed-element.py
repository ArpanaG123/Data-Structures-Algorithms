# Find K Closest Elements
# Link - https://leetcode.com/problems/find-k-closest-elements/description/

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


arr = [1,2,3,4,5]
k = 4
x = 3
# Output: [1,2,3,4]

arr = [1,1,2,3,4,5]
k = 4
x = -1
# Output: [1,1,2,3]

# Approach1 - using two pointers

def findClosestElements(arr,k,x):
    n = len(arr)

    i = 0
    j = n-1

    while j - i + 1 > k:
        if abs(arr[i] - x) > abs(arr[j] - x):
            i += 1
        elif abs(arr[i] - x) < abs(arr[j] - x):
            j -= 1
        else:
        # If the absolute differences are the same, prefer the smaller value
            if arr[i] < arr[j]:
                j -= 1
            else:
                i += 1

    return arr[i:j+1]
