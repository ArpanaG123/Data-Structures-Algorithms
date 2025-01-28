# Infix to Prefix conversion

def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0
    
def InfixtoPrefix(s):
    s = s[::-1]
    s = s.replace('(', 'temp').replace(')', '(').replace('temp', ')')
 
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
    return ans[::-1]

s = "(a+b)*c-d+f"    
result = InfixtoPrefix(s)
print(result)