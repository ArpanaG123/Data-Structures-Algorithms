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

# Initialize the input list
nums = [2, 3, -2, 4]

# Get the length of the input list
n = len(nums)

# Initialize prefix and suffix products to 1
# These will be used to calculate the product of subarrays starting from the left and right, respectively
prefix = 1
suffix = 1

# Initialize maxi to negative infinity to store the maximum product found
maxi = float('-inf')

# Loop through the array to calculate prefix and suffix products
for i in range(0, n):
    # If the prefix product becomes 0, reset it to 1 to start fresh
    if prefix == 0:
        prefix = 1
    
    # If the suffix product becomes 0, reset it to 1 to start fresh
    if suffix == 0:
        suffix = 1
    
    # Update the prefix product by multiplying the current element from the left
    prefix *= nums[i]
    
    # Update the suffix product by multiplying the current element from the right
    suffix *= nums[n - i - 1]
    
    # Update the maximum product found so far, comparing the current prefix and suffix products
    maxi = max(maxi, max(prefix, suffix))

# Print the maximum product of any subarray
print(maxi)

# Time Complexity: O(n) - We iterate through the array once.
# Space Complexity: O(1) - We use constant space for variables like prefix, suffix, and maxi.



# Intuition:
# The main idea behind this approach is to compute the product of subarrays in two directions:

# Prefix product: Start multiplying elements from the left to the right (like a forward pass).
# Suffix product: Start multiplying elements from the right to the left (like a backward pass).
# This is important because:

# Negative numbers: In a product, negative numbers can flip the sign of the result. So, you may get a larger product by considering products from both directions.
# Zeros: Zeros can "reset" the product, so when a zero is encountered, we reset the product and continue. This ensures that subarrays after a zero are also considered.




