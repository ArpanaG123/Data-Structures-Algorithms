# Factorial of a number using recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n-1)

n = 5  
result = fact(n)
print(result)

# Using loop
def fact(n):

    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans

n = 5  
result = fact(n)
print(result)
