# Print all Divisors of a given Number

# Problem Statement: Given an integer N, return all divisors of N.

# A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.
# Link - https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1?utm_source=youtube&amp%3Butm_medium=collab_striver_ytdescription&amp%3Butm_campaign=all-divisors-of-a-number



# Brute force
N = 36
divisors = []
for i in range(1,N+1):
    if N % i == 0:
        divisors.append(i)
print(divisors)

# TC = 0(N)

# Optimal
import math

n = 36
divisors = []
for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        divisors.append(i)
        if n//i != i:
            divisors.append(n//i)

divisors.sort()
print(divisors)

# Time Complexity: O(sqrt(N)) where N is the input number. 
# The algorithm iterates through each number from 1 to the square root of N once to check if it is a divisor.