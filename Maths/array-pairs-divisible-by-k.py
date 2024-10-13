# Check If Array Pairs Are Divisible by k
# Link - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.

arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

arr = [1,2,3,4,5,6]
k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).

arr = [1,2,3,4,5,6]
k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

# Approach - valid, if array has only +ve elements
def can_partition(arr, k):
    freq = [0] * k

    # Calculate frequencies of remainders
    for num in arr:
        rem = num % k
        freq[rem] += 1

    # Check pairs for remainder 0
    if freq[0] % 2 != 0:
        return False

    # Check pairs for other remainders
    for i in range(1, (k // 2) + 1):
        if freq[i] != freq[k - i]:
            return False
    
    return True

# Example usage
arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
result = can_partition(arr, k)
print(result)  # Output:True

# approach for -ve and +ve elements
def can_be_paired(arr, k):
    n = len(arr)
    freq = [0] * k

    for num in arr:
        rem = num % k
        # Adjust negative remainders to be positive
        if rem < 0:
            rem += k
        freq[rem] += 1

    # Check if there's an odd number of elements with remainder 0
    if freq[0] % 2 != 0:
        return False

    # Check pairs from 1 to k//2
    for i in range(1, (k // 2) + 1):
        if freq[i] != freq[k - i]:
            return False
    return True

# Test case with negative elements
arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9, -2, -3]
k = 5
result = can_be_paired(arr, k)
print(result) 

