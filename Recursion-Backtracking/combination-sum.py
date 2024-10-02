# Combination Sum
# Link - https://leetcode.com/problems/combination-sum/description/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


candidates = [2,3,6,7]
target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

def combinationSum(candidates,target):
    ans = []
    n = len(candidates)
    
    def helper(idx,arr,temp,target):
        
        if target == 0:
            ans.append(temp[:])
            return
        
        if idx == n or target < 0:
            return 
        
        # Exclude the current element and move to the next
        helper(idx+1,arr,temp,target)
        
        # Include the current element and allow its reuse
        temp.append(arr[idx])
        helper(idx,arr,temp,target-arr[idx])
        
        #Backtrack
        temp.pop()
    
    helper(0,candidates,[],target)
    return ans

candidates = [2,3,6,7]
target = 7
result = combinationSum(candidates,target)
print(result)