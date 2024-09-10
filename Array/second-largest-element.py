# Find Second Smallest and Second Largest Element in an array
# Link - https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest

# Approach1 - using sorting(only applicable if array has unique elements means no duplicate)

arr = [12, 35, 1, 10, 34, 1]

arr.sort()

print(arr[-2])

# TC = 0(nlogn)
# SC = 0(n)

# Approach2 - Better
arr = [12, 35, 1, 10, 34, 1]
n = len(arr)

small = float('inf')
second_small = float('inf')
large = float('-inf')
second_large = float('-inf')

for i in range(0,n):
    small = min(small,arr[i])
    large = max(large,arr[i])

for i in range(0,n):
    if arr[i] > small and arr[i] < second_small:
        second_small = arr[i]
    
    if arr[i] < large and arr[i] > second_large:
        second_large = arr[i]
print(second_small)
print(second_large)

# Time Complexity: O(N), We do two linear traversals in our array
# Space Complexity: O(1)

# Approach3 - Optimal and Best

arr = [12, 35, 1, 10, 34, 1]

n = len(arr)
small = float('inf')
second_small = float('inf')
large = float('-inf')
second_large = float('-inf')

for i in range(0,n):
    if arr[i] < small:
        second_small = small
        small = arr[i]
    elif arr[i] > small and arr[i] < second_small:
        second_small = arr[i]
print(second_small)

for i in range(0,n):
    if arr[i] > large:
        second_large = large
        large = arr[i]
    elif arr[i] < large and arr[i] > second_large:
        second_large = arr[i]
print(second_large)

# Time Complexity: O(N)
# Space Complexity: O(1)
