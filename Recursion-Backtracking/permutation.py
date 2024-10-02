# Permutations
# Link - https://leetcode.com/problems/permutations/description/

# Given an array nums of distinct integers, return all the possible 
# permutations.You can return the answer in any order.

nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums = [0,1]
# Output: [[0,1],[1,0]]

def permute(nums):
    n = len(nums)
    ans = []
    
    def helper(idx,nums):
        if idx == n:
            ans.append(nums[:])
            return 
        
        for i in range(idx,n):
            nums[i],nums[idx] = nums[idx],nums[i]
            helper(idx+1,nums)
            nums[i],nums[idx] = nums[idx],nums[i]
            
    helper(0,nums)
    ans.sort()
    return ans
            

nums = [1,2,3]
result = permute(nums)
print(result)

# unique permutation
# Link - https://leetcode.com/problems/permutations-ii/

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

def permute(nums):
    n = len(nums)
    ans = []
    
    nums.sort()
    
    def helper(idx,nums):
        if idx == n:
            ans.append(nums[:])
            return 
        
        seen = set()
        for i in range(idx,n):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            nums[i],nums[idx] = nums[idx],nums[i]
            helper(idx+1,nums)
            nums[i],nums[idx] = nums[idx],nums[i]
             
    helper(0,nums)
    return ans
            

nums = [1,1,2]
result = permute(nums)
print(result)
