# Power of 3
# Link - https://leetcode.com/problems/power-of-three/description/

n = 16
# output = False

n = 27
# Output = True

if n <= 0:
    print(False)

while n % 3 == 0:
    n = n//3

if n == 1:
    print(True)
else:
    print(False)

# TC = 0(nlogn) - with base3
# SC = 0(1)