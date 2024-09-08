# Number of Even and Odd Bits
# You are given a positive integer n.
# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.
# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.
# Return an integer array answer where answer = [even, odd].


n = 17
# Output: [2,0]

n = 17
even = 0
odd = 0

res = []
while n != 0:
    if n%2 == 1:
        res.append("1")
    else:
        res.append("0")

    n = n//2

binary = "".join(res)
print(binary)

for i in range(0,len(binary)):
    if binary[i] == "1":
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
print([even,odd])
