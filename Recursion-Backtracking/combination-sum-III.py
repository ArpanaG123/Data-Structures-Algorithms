# Combination Sum III
# Link - https://leetcode.com/problems/combination-sum-iii/description/

# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


k = 3
n = 7
# Output: [[1,2,4]]
# Explanation: 1 + 2 + 4 = 7
# There are no other valid combinations.

def combinationSum3(k,n):
    
    ans = []
    
    def helper(idx,sm,temp,k,n):
        if sm == n and k == 0:
            ans.append(temp[:])
            return 
        
        if sm > n or k < 0:
            return 
        
        for i in range(idx,10):
            temp.append(i)
            helper(i + 1, sm + i, temp, k - 1, n)
            temp.pop()
    
    helper(1,0,[],k,n)
    return ans
    
k = 3
n = 9
result = combinationSum3(k,n)
print(result)