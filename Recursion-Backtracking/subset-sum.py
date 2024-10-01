# Subset Sums
# Given a list arr of n integers, return sums of all subsets in it. Output sums can be printed in any order.

# link - https://www.geeksforgeeks.org/problems/subset-sums2234/1

n = 2
arr = [2, 3]
# Output: 0 2 3 5
# Explanation: When no elements is taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When element 2 and 3 are taken then Sum = 2+3 = 5.


n = 3
arr = [1, 2, 1]
# Output: 0 1 1 2 2 3 3 4

# Brute force
arr = [2,3]

def generateSubsetsSum(arr):
    n = len(arr)
    ans = []
    total_subsets = 1<<n
    
    for i in range(total_subsets):
        subsets = []
        sm = 0
        for j in range(n):
            if i & (1<<j):
                subsets.append(arr[j])
                sm = sum(subsets)
        ans.append(sm)
    return ans
    
res = generateSubsetsSum(arr)
print(res)

# TC = 0(2^N * N)

# Optimal - using recursion
arr = [1,2,3]
n = len(arr)

def subsetSum(arr,n):
    ans = []
    
    def subsetSumHelper(idx,sm):
        if idx == n:
            ans.append(sm)
            return 
        
        subsetSumHelper(idx+1,sm + arr[idx])
        
        subsetSumHelper(idx+1,sm)
        
    subsetSumHelper(0,0)
    ans.sort()
    return ans
    
result = subsetSum(arr,n)
print(result)

# TC = 0(2^N) + 0(2^n log 2^n)
# sc = 0(1)

# If ans need in sorted order then use sorting else not use it.
# TC without sorting will be 0(2^n)
