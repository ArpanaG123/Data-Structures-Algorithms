# Find the maximum and minimum element in an array.
# Link - https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

arr = [3, 5, 4, 1, 9]
# Output: 
# Minimum element is: 1
# Maximum element is: 9

# Method1
arr = [3,5,4,1,9]
n = len(arr)

arr.sort()
print("Minimum element is: ",arr[0])
print("Maximum element is: ",arr[n-1])

# TC = O(n log n)
# SC = 0(1)

# Method2
arr = [3,5,4,1,9]

mx = arr[0]
mn = arr[0]

n = len(arr)

for i in range(1,n):
    mx = max(mx,arr[i])
    mn = min(mn,arr[i])
print("Minimum element is: ",mn)
print("Maximum element is: ",mx)

# Time Complexity: O(n)
# Space Complexity: O(1) - The code uses a fixed amount of extra space to store the variables mx, mn, and n. These variables do not depend on the size of the input list, so the space complexity is O(1).

