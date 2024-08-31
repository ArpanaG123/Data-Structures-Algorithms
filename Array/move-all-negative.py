# Move all the negative elements to one side of the array. 
# Link - https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/


arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6 ]
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# Method1

arr = [-12,11,-13,-5,6,-7,5,-3,-6]

arr.sort()
print(arr)

# TC = 0(NlogN)
# SC = 0(1)

# Method2 - Efficient approach  - Quick sort
arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6 ]
n = len(arr)

j = 0
for i in range(0,n):
    if arr[i] < 0:
        arr[i],arr[j] = arr[j],arr[i]
        j += 1
    

print(arr)

# TC = 0(N)
# SC = 0(1)

