# Combination Sum II
# Link - https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

candidates = [10,1,2,7,6,1,5]
target = 8
# Output: 
# [[1,1,6],
# [1,2,5],
# [1,7],
# [2,6]]

def combinationSum2(candidates,target):
    
    candidates.sort()
    ans = []
    n = len(candidates)
    
    def helper(idx,temp,target):
        
        if target == 0:
            ans.append(temp[:])
            return
        
        for i in range(idx,n):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] > target:
                break
        
            # Include the current element and allow its reuse
            temp.append(candidates[i])
            helper(i+1,temp,target-candidates[i])
            #Backtrack
            temp.pop()
    
    helper(0,[],target)
    return ans

candidates = [10,1,2,7,6,1,5]
target = 8
result = combinationSum2(candidates,target)
print(result)
