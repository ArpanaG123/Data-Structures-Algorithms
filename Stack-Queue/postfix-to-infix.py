# Postfix to Infix Conversion
# Link - https://www.geeksforgeeks.org/problems/postfix-to-infix-conversion/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=postfix-to-prefix-conversion

# You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.
# Input:ab*c+ 
# Output: ((a*b)+c)
# Explanation: The above output is its valid infix form.

def PostfixToInfix(s):
    
    st = []
    n = len(s)
    
    i = 0
    
    while i < n:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9") or (s[i] >= "a" and s[i] <= "z"):
            st.append(s[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            converted_s = "(" + t2 + s[i] + t1 + ")"
            st.append(converted_s)
        i += 1
        
    return st[-1]

s = "ab-de+f*/"    
result = PostfixToInfix(s)
print(result)