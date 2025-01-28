# Postfix to Prefix Conversion
# Link - https://www.geeksforgeeks.org/problems/postfix-to-prefix-conversion/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=postfix-to-prefix-conversio

# You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.


# Input: ABC/-AK/L-*
# Output: *-A/BC-/AKL
# Explanation: The above output is its valid prefix form.



def PostfixToPrefix(s):
    
    st = []
    n = len(s)
    i = 0
    
    while i < n:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9") or (s[i] >= "a" and s[i] <= "z"):
            st.append(s[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            converted_s = s[i] + t2 + t1
            st.append(converted_s)
        i += 1
        
    return st[-1]

s = "AB-DE+F*/"    
result = PostfixToPrefix(s)
print(result)