# Combinations
# link - https://leetcode.com/problems/combinations/description/?envType=problem-list-v2&envId=backtracking&difficulty=MEDIUM

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

n = 4
k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

def combine(n,k):
    ans = []

    def helper(idx,temp):
        if len(temp) == k:
            ans.append(temp[:])
            return 
            
        for i in range(idx,n+1):
            temp.append(i)
            helper(i+1,temp)
            temp.pop()
        
    helper(1,[])
    return ans

n = 4, k = 2
result = combine(n,k)
print(result)

# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]