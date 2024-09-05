# Count Trailing Zeroes

n = 12
# output = 2
# Explanation 1: The binary representation of the number 12 is “1100”. Therefore, there are two trailing zeros in the 12.

# Method1 - Brute force

n = 12
bit = []
while n != 0:
    if n % 2 == 1:
        bit.append("1")
    else:
        bit.append("0")
    n = n//2

bit.reverse()
bits = "".join(map(str,bit))

length = len(bit)

cnt = 0
for i in range(length-1,-1,-1):
    if bit[i] == "0":
        cnt += 1
    else:
        break
print(cnt)

# TC = 0(N)
# SC = 0(N)


# Method2 - Bitwise

n = 12
cnt = 0

while n&1 == 0:
    n = n>>1
    cnt += 1
print(cnt)

# TC = 0(1)
# SC = 0(1)