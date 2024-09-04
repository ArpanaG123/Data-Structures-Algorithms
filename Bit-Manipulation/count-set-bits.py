# Number of 1 Bits
# Write a function that takes the binary representation of a positive integer and returns the number of 
# set bits it has (also known as the Hamming weight).

# Input: 
n = 11

# Output: 3
# Explanation:The input binary string 1011 has a total of three set bits.

# Method1 = Brute force
n = 11

bits = []

while n != 0:
    if n % 2 == 1:
        bits.append("1")
    else:
        bits.append("0")
    n = n//2

bits.reverse()

count = 0
for i in bits:
    if i == "1":
        count += 1
print(f"Number of set bits are: {count}")

# TC = 0(N LOG N)
# SC = 0(N)

# Method2 - Better
n = 11
count = 0
while n != 0:
    n = n & (n-1)
    count += 1
print(f"Number of set bits are: {count}")

# TC = 0(1)
# sc = 0(1)

# Method3 - Optimal

n = 11

count = 0
while n != 0:
    if n&1 == 1:
        count += 1
    n = n>>1
print(f"Number of set bits are: {count}")

# TC = 0(1)
# sc = 0(1)

# Type2 - question
# Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Input: 
n = 2
# Output: [0,1,1]

n = 2
ans = []

for i in range(0,n+1):
    bits = i
    
    count = 0
    
    while bits != 0:
        bits = bits & bits-1
        count += 1
    ans.append(count)
print(ans)

# Type3 - 
s = "00000000000000000000000000001011"
# Output 1: 3
# Explanation 1: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

n = int(s,2)

count = 0

while n != 0:
    if n&1 == 1:
        count += 1
                
    n = n >> 1

print(f"Number of set bits are: {count}")
