# Maximum Product Subarray
# Link1 - https://leetcode.com/problems/maximum-product-subarray/description/
# Link2 - https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1

# Method1 - brute force

nums = [2,3,-2,4]
n = len(nums)

res = []
maxi = float('-inf')
for i in range(0,n):
    for j in range(i,n):
        prod = 1
        for k in range(i,j+1):
            prod  *= nums[k]
            maxi = max(prod,maxi)
            res.append(maxi)

print(maxi)
# print(res)
# print(max(res))

# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Better approach
nums = [2, 3, -2, 4]
n = len(nums)

res = []
maxi = float('-inf')
for i in range(0, n):
    prod = 1
    for j in range(i, n):
        prod *= nums[j]
        maxi = max(maxi, prod)
        res.append(maxi)
print(maxi)
# print(res)
# print(max(res))

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Method3 - Optimal Approach - observation based 

nums = [2, 3, -2, 4]
n = len(nums)
prefix = 1
suffix = 1
maxi = float('-inf')

for i in range(0,n):
    if prefix == 0:
        prefix = 1
    if suffix == 0:
        suffix = 1
    
    prefix *= nums[i]
    suffix *= nums[n-i-1]
    
    maxi = max(maxi,max(prefix,suffix))
print(maxi)

# Time Complexity: O(n)
# Space Complexity: O(1)




