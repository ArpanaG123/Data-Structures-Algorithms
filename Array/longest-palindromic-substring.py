# Longest Palindromic Substring

# Link - https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, return the longest palindromicsubstring in s.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

s = "cbbd"
# Output: "bb"

# Approach1:

def is_plaindrome(s,left,right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True
    
def longestPalindrome(s):
    n = len(s)
    longest = ""
    
    if n < 2:
        return s
    
    for i in range(n):
        for j in range(i,n):
            if is_plaindrome(s,i,j):
                if j - i + 1 > len(longest):
                    longest = s[i:j+1]
    return longest

s = "babad"
result = longestPalindrome(s)
print(result)

# TC = 0(N^3)

# Approach2 - Optimised - using DP

