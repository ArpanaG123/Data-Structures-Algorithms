# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Link - https://leetcode.com/problems/missing-number/description/

 

# Example:
nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Mathematical approach

def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2  # Sum of numbers from 0 to n
    actual_sum = sum(nums)         # Sum of the numbers in the list
    return total_sum - actual_sum  # The difference is the missing number

# Example usage
nums = [3, 0, 1]
print(missingNumber(nums))  # Output will be 2


# using Set approach
def missingNumber(nums):
    n = len(nums)
    num_set = set(nums)
    for i in range(n + 1):
        if i not in num_set:
            return i

# Example usage
nums = [3, 0, 1]
print(missingNumber(nums))  # Output will be 2

# Using sorting approach
def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)  # If no mismatch is found, the missing number is n

# Example usage
nums = [3, 0, 1]
print(missingNumber(nums))  # Output will be 2


# using bit manipulation xor
def missingNumber(nums):
    n = len(nums)
    xor_all = 0
    xor_nums = 0
    
    for i in range(n + 1):
        xor_all ^= i
    
    for num in nums:
        xor_nums ^= num
    
    return xor_all ^ xor_nums

# Example usage
nums = [3, 0, 1]
print(missingNumber(nums))  # Output will be 2
