# Sum of first n terms

# Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.
# Link - https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

n=5
# Output:225
# Explanation:13+23+33+43+53=225

# Parameterised recursion

n = 3
# output = 1+2+3 = 6

n = 3
sm = 0

def sumOfNaturalNumber(n,sm):
    if n <= 0:
        print(sm)
        return 
    
    sumOfNaturalNumber(n-1,sm+n)
    
result = sumOfNaturalNumber(n,sm)

# Functional recursion
n = 3

def sumOfNaturalNumber(n):
    if n <= 0:
        return 0
    
    return n + sumOfNaturalNumber(n-1)
    
result = sumOfNaturalNumber(n)
print(result)