# Maximum Gap
# Link - https://leetcode.com/problems/maximum-gap/description/


# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time and uses linear extra space.

nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

# Brute force
def maximumGap(nums):
    nums.sort()
    n = len(nums)
    
    if n < 2:
        return 0
        
    diff = 0
    for i in range(1,n):
        diff = max(diff,(nums[i] - nums[i-1]))
    return diff

nums = [3,6,9,1]   
result = maximumGap(nums)
print(result)

# TC = 0(N)+0(nlogn)
# SC = 0(1)

# Optimal approach
# Pigeonhole Principle Approach to Solve Maximum Gap Problem

# statement
# The Pigeonhole Principle states that if n items are put into m containers, with n>m, then at least one container must contain more than one item. We can apply this principle to the maximum gap problem in a way similar to bucket sort, but without the explicit sorting within buckets.

import math

def maximumGap(nums):
    if len(nums) < 2:
        return 0
    
    # Step 1: Find the minimum and maximum values
    min_val, max_val = min(nums), max(nums)

    # If all elements are the same, the gap is 0
    if min_val == max_val:
        return 0

    n = len(nums)

    # Step 2: Calculate bucket size
    bucket_size = math.ceil((max_val - min_val) / (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    # Initialize buckets
    buckets_min = [float('inf')] * bucket_count
    buckets_max = [-float('inf')] * bucket_count

    # Step 3: Place each number in its corresponding bucket
    for num in nums:
        # Find the appropriate bucket index
        bucket_idx = (num - min_val) // bucket_size
        
        # Update the bucket's min and max
        buckets_min[bucket_idx] = min(buckets_min[bucket_idx], num)
        buckets_max[bucket_idx] = max(buckets_max[bucket_idx], num)

    # Step 4: Compute the maximum gap
    max_gap = 0
    previous_max = min_val  # Start with the min value

    for i in range(bucket_count):
        # Skip empty buckets
        if buckets_min[i] == float('inf') and buckets_max[i] == -float('inf'):
            continue
        
        # The gap is the difference between the min of the current bucket and the max of the previous bucket
        max_gap = max(max_gap, buckets_min[i] - previous_max)
        previous_max = buckets_max[i]

    return max_gap

# Test case
nums = [3, 6, 9, 1]
print(maximumGap(nums))
