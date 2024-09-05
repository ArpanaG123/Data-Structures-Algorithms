# Alternate Bit
# Check if a number has bits in an alternate pattern.

n = 10
# Output 1: true
# Explanation 1: 10 in binary = (1010), has an alternate pattern.

n = 42

if n & n>>1 == 0:
    print(True)
else:
    print(False)