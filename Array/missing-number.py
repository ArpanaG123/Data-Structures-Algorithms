# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Link = https://leetcode.com/problems/missing-number/description/
 

# Example 1:
arr = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


# Brute force
arr = [1,2,4,5]

def missingNumber(arr):
    n = len(arr)
    
    for i in range(1,n+1):
        flag = 0
        for j in range(0,n):
            if arr[j] == i:
                flag = 1
                break
    
        if flag == 0:
            return i
    return -1

result = missingNumber(arr)
print(result)

# TC = 0(N*N)
# SC = 0(1)

# Better - using hashmap

arr = [1,2,4,5]
n = len(arr)
mx = max(arr)

freq = [0]*(mx+1)

for i in range(0,n):
    freq[arr[i]] = 1


for i in range(1,len(freq)):
    if freq[i] == 0:
        print(i)

# TC = 0(N) + 0(N)
# SC = 0(N) - bcoz of hashing

# Optimal solution
nums = [3,0,1]
n = len(nums)
        
total_sum = n * (n+1)//2
actual_sum = sum(nums)

print(total_sum - actual_sum)

# TC = 0(N)
# SC = 0(1)

# optimal2 - using bit manipulation xor
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