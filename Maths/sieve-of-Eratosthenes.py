# Sieve of Eratosthenes
# Given a number n, print all prime number till n.

n = 10
# output - 2,3,5,7

# Approach1
import math

def is_prime(n):
    count = 0
    
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            count += 1
            if i != n//i:
                count +=1 
    
    if count == 2:
        return True
    else:
        return False

def print_prime_factors(n):
    prime = []
    for i in range(2,n+1):
        if is_prime(i):
            prime.append(i)
    return len(prime)

# Total count of prime from 1 to n
n = 10
result = print_prime_factors(n)
print(result)

# TC = 0(N * sqrt(N))
# sc = 0(1)

# Using alogoithm - seive of erathosense

def count_prime(n):
    
    is_prime = [True] * (n+1)
    
    i = 2
    while i*i <= n:
        if is_prime[i]:
            for j in range (i*i,n+1,i):
                is_prime[j] = False
        i += 1
        
    primes = [i for i in range(2,n+1) if is_prime[i]]
    return len(primes)

n = 11
result = count_prime(n)
print(result)
# output = 5 = (2,3,5,7,11)

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
