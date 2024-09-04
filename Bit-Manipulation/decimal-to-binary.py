# Decimal to binary conversion

n = 10

res = []

while n != 0:
    if n%2 == 0:
        res.append("0")
    else:
        res.append("1")
    n = n//2

res.reverse()
print("".join(res))

# TC = 0(log N) - as every time n divides by 2