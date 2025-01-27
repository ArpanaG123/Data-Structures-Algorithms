# Infix to Postfix conversion
# Link - https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=infix-to-postfix

# Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.
# Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
# Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
# Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.

# Examples :
# Input: s = "a+b*(c^d-e)^(f+g*h)-i"
# Output: abcd^e-fgh*+^*+i-
# Explanation: After converting the infix expression into postfix expression, the resultant expression will be abcd^e-fgh*+^*+i-



def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

   
def InfixtoPostfix(s):
    ans = ""
    st = []
    n = len(s)
    
    i = 0
    while i < n:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9") or (s[i] >= "a" and s[i] <= "z"):
            ans += s[i]
        elif s[i] == "(":
            st.append(s[i])
        elif s[i] == ")":
            while (len(st) != 0 and st[-1] != "("):
                ans += st.pop()
            st.pop()
        else:
            while (len(st) != 0 and priority(s[i]) <= priority(st[-1])):
                ans += st.pop()
            st.append(s[i])
        i += 1
        
    while (len(st) != 0):
        ans += st.pop()
    return ans

s = "a+b*(c^d-e)^(f+g*h)-i"    
result = InfixtoPostfix(s)
print(result)
        