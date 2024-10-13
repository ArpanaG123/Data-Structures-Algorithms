# Print all prime factors of a Number.
import math

n = 6
# output - 2,3,5

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
    return prime

# print prime from 1 to n
n = 11
result = print_prime_factors(n)
print(result)

# using sieve of erathosesne


def print_prime(n):
    
    is_prime = [True] * (n+1)
    
    i = 2
    while i*i <= n:
        if is_prime[i]:
            for j in range (i*i,n+1,i):
                is_prime[j] = False
        i += 1
        
    primes = [i for i in range(2,n+1) if is_prime[i]]
    return primes

n = 11
result = print_prime(n)
print(result)
