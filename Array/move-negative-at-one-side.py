# Move all negative numbers to beginning and positive to end with constant extra space

# Link - https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6]
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# Approach1 - Brute force
arr.sort()
print(arr)

# Time Complexity: O(n*log(n)), Where n is the length of the given array.
# Auxiliary Space: O(1)

# Approach2 - Efficient - Two pointer

arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6]

def shiftall(arr):
    n = len(arr)
    i = 0
    j = n-1
    
    while i <= j:
        if arr[i] < 0 and arr[j] < 0:
            i += 1
        elif arr[i] > 0 and arr[j] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
        elif arr[i] > 0 and arr[j] > 0:
            j -= 1
        elif arr[i] < 0 and arr[j] > 0:
            i += 1
            j -= 1
            
    return arr

result = shiftall(arr)
print(result)

# TC = 0(N)
# SC = 0(1)
