# Prefix to Infix Conversion
# Link - https://www.geeksforgeeks.org/problems/prefix-to-infix-conversion/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=prefix-to-infix-conversion

# You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form.

# Input: *-A/BC-/AKL
# Output: ((A-(B/C))*((A/K)-L))
# Explanation: The above output is its valid infix form.

def PrefixToInfix(s):
    
    st = []
    n = len(s)
    i = n-1
    
    while i >= 0:
        if (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9") or (s[i] >= "a" and s[i] <= "z"):
            st.append(s[i])
        else:
            t1 = st.pop()
            t2 = st.pop()
            converted_s = "(" + t1 + s[i] + t2 + ")"
            st.append(converted_s)
        i -= 1
        
    return st[-1]

s = "*+PQ-MN"    
result = PrefixToInfix(s)
print(result)