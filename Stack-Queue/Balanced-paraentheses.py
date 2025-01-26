# Balanced or valid paraentheses
# Link - https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Examples:
# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false


def validParentheses(s):
    stack = []
    
    n = len(s)
    
    for i in range(n):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (s[i] == ")" and top != "(") or (s[i] == "]" and top != "[") or (s[i] == "}" and top != "{"):
                return False
    
    return len(stack) == 0
    
s = "(]"
res = validParentheses(s)
print(res)