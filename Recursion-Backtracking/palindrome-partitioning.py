# Palindrome Partitioning
# Link - https://leetcode.com/problems/palindrome-partitioning/description/

# Given a string s, partition s such that every substring of the partition is a palindrome
# Return all possible palindrome partitioning of s.

s = "aab"
# Output: [["a","a","b"],["aa","b"]]

s = "a"
# Output: [["a"]]

def partition(s):
    n = len(s)
    ans = []
    
    def is_plaindrome(s):
        n = len(s)
        start = 0
        end = n-1
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        
    
    def helper(idx,s,temp):
        if idx == n:
            ans.append(temp[:])
            return 
        
        for i in range(idx,n):
            if is_plaindrome(s[idx:i+1]):
                temp.append(s[idx:i+1])
                helper(i+1,s,temp)
                temp.pop()
    
    helper(0,s,[])
    return ans
            

s = "aabb"
result = partition(s)
print(result)