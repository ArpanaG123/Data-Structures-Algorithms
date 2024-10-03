# Subsets
# link - https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, return all possible subsets(the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [0]
# Output: [[],[0]]

def subsets(arr):
    n = len(arr)
    ans = []
    
    def helper(idx,arr,temp):
        
        ans.append(temp[:])
        
        for i in range(idx,n):
            temp.append(arr[i])
            helper(i+1,arr,temp)
            temp.pop()
            
    helper(0,arr,[])
    return ans

arr = [1,2,3]
result = subsets(arr)
print(result)