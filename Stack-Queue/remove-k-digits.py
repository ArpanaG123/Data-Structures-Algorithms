# Remove K Digits
# Link - https://leetcode.com/problems/remove-k-digits/description/

# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

def removeKdigits(num, k):
    st = []
    n = len(num)
    
    for i in range(n):
        # While the stack is not empty, and the current character is smaller than the top of the stack
        # and we still have digits to remove (k > 0), we pop the stack
        while len(st) != 0 and k > 0 and int(st[-1]) > int(num[i]):
            st.pop()
            k -= 1
        st.append(num[i])
    
    # If we still have k digits to remove, remove them from the end
    while k > 0:
        st.pop()
        k -= 1

    # Convert the list of characters back to a string and strip leading zeros
    result = ''.join(st).lstrip('0')

    # Return the result, or "0" if the result is an empty string
    return result if result != '' else '0'

# Test case
num = "1432219"
k = 3
result = removeKdigits(num, k)
print(result)  # Output should be "1219"