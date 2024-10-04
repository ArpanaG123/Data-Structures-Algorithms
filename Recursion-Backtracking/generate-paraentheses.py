# Generate Parentheses
# Link - https://leetcode.com/problems/generate-parentheses/description/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

n = 3

def generateParenthesis(n):
    ans = []
    
    def backtrack(ans,n,open_count,close_count,s):
        if open_count == close_count == n:
            ans.append(s)
            return 
        
        if open_count < n:
            backtrack(ans,n,open_count+1,close_count,s+"(")
        
        if open_count > close_count:
            backtrack(ans,n,open_count,close_count+1,s+")")
    
    backtrack(ans,n,0,0,"")
    return ans

n = 3   
result = generateParenthesis(n)
print(result)