# Print all prime factors of a Number.
import math

n = 60
# output - 2,3,5

def isPrime(n):
    cnt = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            cnt += 1

            if n//i != i:
                cnt += 1
    
    if cnt == 2:
        return True
    else:
        return False

ans = []  
for i in range(2,n):
    if n % i == 0:
        if isPrime(i):
            ans.append(i)
print(ans)