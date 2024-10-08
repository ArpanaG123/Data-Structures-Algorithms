# Remove Invalid Parentheses
# link - https://leetcode.com/problems/remove-invalid-parentheses/description/?envType=problem-list-v2&envId=backtracking&difficulty=HARD

# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
s = "()())()"
# Output: ["(())()","()()()"]

def removeInvalidParentheses(s):
    ans = []
    
    def getMinInvalid(s):
        st = []
        for char in s:
            if char == "(":
                st.append("(")
            elif char == ")":
                if st and st[-1] == "(":
                    st.pop()
                else:
                    st.append(")")
        return len(st)
    
    def helper(s, min_invalid, visited):
        if min_invalid == 0:
            if getMinInvalid(s) == 0:
                ans.append(s)
            return
        
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            
            next_str = s[:i] + s[i+1:]
            if next_str not in visited:
                visited.add(next_str)
                helper(next_str, min_invalid - 1, visited)
    
    min_invalid = getMinInvalid(s)
    visited = set()
    visited.add(s)
    helper(s, min_invalid, visited)
    return ans

# Example usage
s = "()())()"
res = removeInvalidParentheses(s)
print(res)