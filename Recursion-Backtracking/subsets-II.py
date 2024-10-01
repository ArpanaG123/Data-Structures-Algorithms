# Subsets II

# Given an integer array nums that may contain duplicates, return all possible 
# subsets(the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Link - https://leetcode.com/problems/subsets-ii/description/

nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

nums = [0]
# Output: [[],[0]]

# Approach1 - using bit manipulation
nums = [1,2,2]
def subsetsWithDup(nums):
    n = len(nums)

    total = 1<<n
    ans = set()

    for i in range(total):
        subsets = []
        for j in range(n):
            if i & (1<<j):
                subsets.append(nums[j])
        ans.add(tuple(sorted(subsets)))

    result = sorted([list(x) for x in ans])
    return result

res = subsetsWithDup(nums)
print(res)

# TC = 0(2^n) + 0(2^n log 2^n)
# second will be putting ans into set

# Approach2
# Generate subsets
arr = [1,2,2]
n = len(arr)

def generateSubset(arr,n):
    ans = set()
    
    def generateSubsetHelper(idx,current):
        if idx == n:
            ans.append(tuple(sorted(current)))
            return 
    
        # Exclude
        generateSubsetHelper(idx+1,current)
        
        # Include
        generateSubsetHelper(idx+1,[arr[idx]] + current)
        
    generateSubsetHelper(0,[])
    return [list(t) for t in ans]
    
result = generateSubset(arr,n)
print(result)

# TC = 0(2^n) + 0(mlog m)
# where m is the size of subsets

# Approach3
def generateSubset(arr):
    arr.sort()  # Sort the array to handle duplicates
    ans = []

    def generateSubsetHelper(idx, current):
        # Add the current subset to the result
        ans.append(current[:])
        
        for i in range(idx, len(arr)):
            # Skip duplicates
            if i > idx and arr[i] == arr[i - 1]:
                continue
                
            # Include arr[i] in the current subset
            current.append(arr[i])
            generateSubsetHelper(i + 1, current)
            
            # Backtrack: Remove the last added element
            current.pop()

    # Start the backtracking process
    generateSubsetHelper(0, [])
    return ans

# Example usage
arr = [1, 2, 2]
result = generateSubset(arr)
print(result)

# O(nlogn)+O(n×2^n)=O(n×2^n)
