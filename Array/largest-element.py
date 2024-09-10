# Largest Element in Array
# Link - https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-element-in-array

arr = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.

# Method1 - Brute force
arr = [1, 8, 7, 56, 90]

arr.sort()
n = len(arr)

print(arr[n-1])

# TC = 0(NlogN)
# SC = 0(N)

# METHOD2 - USING Maximum variable

def largest(arr):
    # code here
    mx = arr[0]
        
    n = len(arr)
        
    for i in range(0,n):
        if arr[i] > mx:
            mx = arr[i]
        
    return mx

arr = [1, 8, 7, 56, 90]
result = largest(arr)
print(result)

# TC = 0(N)
# SC = 0(1)

