# Remove Duplicate Letters

# Link - https://leetcode.com/problems/remove-duplicate-letters/description/

# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

def removeDuplicateLetters(s):
    
    n = len(s)
    
    last_idx_arr = [0]*26
    seen = [False]*26
    
    stack = []
    
    for i in range(n):
        last_idx_arr[ord(s[i]) - ord('a')] = i
     
    i = 0   
    while i < n:
        idx = ord(s[i]) - ord('a')
        
        if seen[idx]:
            i += 1
            continue
        
        # chek if stack is not empty and top element of stack is greater then curr elementof string and curr index is less than last index of array so remove element from stack
        while len(stack) > 0 and stack[-1] > s[i] and last_idx_arr[ord(stack[-1]) - ord('a')] > i:
            top = stack.pop()
            seen[ord(top) - ord('a')] = False
        
        stack.append(s[i])
        seen[idx] = True
        i += 1
    return "".join(stack)

s = "cbacdcbc"   
result = removeDuplicateLetters(s)
print(result)