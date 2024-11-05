# Common in 3 Sorted Arrays
# Link - https://www.geeksforgeeks.org/problems/common-elements1132/1


# You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# If there are no such elements return an empty array. In this case, the output will be -1.
# Note: can you handle the duplicates without using any additional Data Structure?

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output: [20, 80]
# Explanation: 20 and 80 are the only common elements in arr, brr and crr.

# Approach1 = three pointer
def findCommon(arr1, arr2, arr3):
    # Initialize pointers for arr1, arr2, arr3
    i = j = k = 0
    
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    
    # Result list to store common elements
    common = []
    
    # Traverse all three arrays simultaneously
    while i < n1 and j < n2 and k < n3:
        # If the elements at i, j, k are equal, it's a common element
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # If arr1[i] is smaller, increment i
        elif arr1[i] < arr2[j]:
            i += 1
        # If arr2[j] is smaller, increment j
        elif arr2[j] < arr3[k]:
            j += 1
        # If arr3[k] is smaller, increment k
        else:
            k += 1
    
    return common

# Test example
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

result = findCommon(arr1, arr2, arr3)
print(result)  # Output: [20, 80]
