# Prefix to Postfix Conversion
# Link - https://www.geeksforgeeks.org/problems/prefix-to-postfix-conversion/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=prefix-to-postfix-conversion

# You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

# Input: *-A/BC-/AKL
# Output: ABC/-AK/L-*
# Explanation: The above output is its valid postfix form.

def PrefixToPostfix(s):
    
    st = []
    n = len(s)
    i = n-1
    
    while i >= 0:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9") or (s[i] >= "a" and s[i] <= "z"):
            st.append(s[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            converted_s = t1 + t2 + s[i]
            st.append(converted_s)
        i -= 1
        
    return st[-1]

s = "/-AB*+DEF"    
result = PrefixToPostfix(s)
print(result)