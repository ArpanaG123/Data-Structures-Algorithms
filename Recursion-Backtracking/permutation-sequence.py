# Permutation Sequence
# Link - https://leetcode.com/problems/permutation-sequence/description/


# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for 
# n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

def getPermutation(n,k):
    
    s = [str(i) for i in range(1, n+1)]
    
    ans = []
    
    def helper(idx,s):
        if idx == n:
            ans.append(''.join(s[:]))
            return 
        
        for i in range(idx,n):
            s[i],s[idx] = s[idx],s[i]
            helper(idx+1,s)
            s[i],s[idx] = s[idx],s[i]
            
    helper(0,s)
    ans.sort()
    return ans[k-1]
            

n = 3
k = 3
result = getPermutation(n,k)
print(result)