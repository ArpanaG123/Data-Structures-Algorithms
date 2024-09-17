# Sieve of Eratosthenes
# Given a number n, print all prime number till n.

n = 10
# output - 2,3,5,7

# Approach1
import math

def isPrimeCheck(n: int) -> bool:
    if n <= 1:
        return False
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
prime = []
def countPrimes(n: int) -> int:
    count = 0
    for i in range(2,n):
        if isPrimeCheck(i):
            prime.append(i)
            count += 1
    return count
    # return prime

n = 10
res = countPrimes(n)
print(res)

# TC = 0(N * sqrt(N))
# sc = 0(1)

# Using alogoithm - 

def count_primes_less_than(n):
    if n <= 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    i = 2
    while i * i < n:
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        i += 1
    
    return sum(is_prime)

# Example usage
n = 3
print(f"Count of prime numbers less than {n}: {count_primes_less_than(n)}")
