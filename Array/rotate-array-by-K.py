# Rotate the array to the right by k steps, where k is non-negative.
# Link - https://leetcode.com/problems/rotate-array/description/

# Example 1:
nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

arr = [1, 2, 3, 4, 5,6,7]
k = 3


n = len(arr)
k = k%n  
# k = k % n: This ensures that the rotation handles cases where k is greater than the length of the array.

arr.reverse()
# print(arr)

arr[0:k] = reversed(arr[0:k])
# print(arr)

arr[k:n] = reversed(arr[k:n])
print(arr)

# TC = 0(N)
# SC = 0(1)