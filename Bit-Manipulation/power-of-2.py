# Power of 2

n = 16
# output = True

# Approach1 
for i in range(0,31):
    ans = 2 ** i

    if ans == n:
        print(True)
print(False)

# TC = 0(31)
# sc = 0(1)

# Approach2
if n > 0 and n & (n-1) == 0:
    print(True)
else:
    print(False)

# TC = 0(1)
# sc = 0(1)

# Approach3
if n <= 0:
    print(False)

cnt = 0
while n != 0:
    n = n & n-1
    cnt += 1
if cnt == 1:
    print(True)
else:
    print(False)
# TC = 0(1)
# sc = 0(1)