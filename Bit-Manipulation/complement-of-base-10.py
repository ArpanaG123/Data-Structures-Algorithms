# Complement of Base 10 Integer
# Link - https://leetcode.com/problems/complement-of-base-10-integer/description/

n = 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

n = 5
num_bit = n.bit_length()

bit_mask = (1 << num_bit) - 1

print(bit_mask ^ n)