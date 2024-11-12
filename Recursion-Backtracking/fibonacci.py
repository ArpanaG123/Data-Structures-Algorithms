# Fibonacci number

# Approach1 - using recursion
def fib(n):
    if n <= 1:
        return n
    
    return fib(n-2) + fib(n-1)
    
n = 3
result = fib(n)
print(result)

# Approach2 - using loop
def fib(n):
    f1 = 0
    f2 = 1
    
    res = []
    
    for i in range(0,n):
        if i == 0:
            res.append(f1)
        elif i == 1:
            res.append(f2)
        else:
            f3 = f1 + f2
            res.append(f3)
            f2 = f3
            f1 = f2
    return res
    
n = 3
result = fib(n)
print(result)