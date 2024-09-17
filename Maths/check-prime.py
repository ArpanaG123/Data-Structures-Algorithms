# Check if a number is prime or not

# Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

# Brute force
n = 6
cnt = 0
for i in range(1,n+1):
    if n % i == 0:
        cnt += 1

if cnt == 2:
    print(True)
else:
    print(False)

# TC = 0(N)


# Optimal
import math
n = 6
cnt = 0
for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        cnt += 1
        if n//i != i:
            cnt += 1

if cnt == 2:
    print(True)
else:
    print(False)

# TC = 0(sqrt(n))