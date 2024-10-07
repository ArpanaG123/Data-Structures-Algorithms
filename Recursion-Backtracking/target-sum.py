# Target Sum
# Link - https://leetcode.com/problems/target-sum/description/

# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

nums = [1,1,1,1,1]
target = 3

# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# code

def findTargetSumWays(nums,target):
    ans = 0
    n = len(nums)
    
    def helper(idx,sm):
        nonlocal ans
        if idx == n:
            if sm == target:
                ans += 1
            return
        
        helper(idx+1,sm + nums[idx])
        helper(idx+1,sm - nums[idx])
    
    helper(0,0)
    return ans
    
nums = [1,1,1,1,1]
target = 3
result = findTargetSumWays(nums,target)
print(result)

# Note:for larger input need DP concept as need memoization.
# This will work only for short Test cases.