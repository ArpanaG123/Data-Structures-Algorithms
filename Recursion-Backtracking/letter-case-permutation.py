# Letter Case Permutation
# Link - https://leetcode.com/problems/letter-case-permutation/description/

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

s = "3z4"
# Output: ["3z4","3Z4"]

def letterCasePermutation(s):
    ans = []
    n = len(s)
    
    def helper(idx,temp):
        if idx == n:
            ans.append(temp)
            return
            
        if s[idx].isalpha():
            helper(idx+1,temp+s[idx].lower())
            helper(idx+1,temp+s[idx].upper())
        else:
            helper(idx+1,temp+s[idx])
            
    helper(0,"")
    return ans

s = "a1b2"
result = letterCasePermutation(s)
print(result)

# Output: ["a1b2","a1B2","A1b2","A1B2"]