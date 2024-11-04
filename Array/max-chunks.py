# Max Chunks To Make Sorted - I
# Link - https://leetcode.com/problems/max-chunks-to-make-sorted/description/

# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.

arr = [4,3,2,1,0]
# Output: 1
# Explanation: Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

def maxChunksToSorted(arr):
    n = len(arr)
        
    pos = 0
    max_so_far = 0

    for i in range(n):
        max_so_far = max(arr[i],max_so_far)

        if max_so_far == i:
            pos += 1
    return pos

arr = [4,3,2,1,0]
result = maxChunksToSorted(arr)
print(result)
# output = 1

# Max Chunks To Make Sorted II
# Link - https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/

# You are given an integer array arr.
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.

arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.


def maxChunksToSorted(arr):
    n = len(arr)

    sorted_arr = sorted(arr)  # Sorted version of the input array

    sum_original = 0  # Sum of elements in the original array
    sum_sorted = 0    # Sum of elements in the sorted array
    
    chunks = 0

    for i in range(n):
        sum_original += arr[i]
        sum_sorted += sorted_arr[i]

        # When the sum of elements so far in the original array matches the sum in the sorted array,
        # it means we can split the array into a chunk here.
        if sum_original == sum_sorted:
            chunks += 1

    return chunks

# Test case
arr = [1, 1, 0, 0, 1]
result = maxChunksToSorted(arr)
print(result)  # Expected output: 2