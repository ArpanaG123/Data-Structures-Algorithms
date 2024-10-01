# Print N to 1 without loop

# Print numbers from N to 1 (space separated) without the help of loops.

# N = 10
# Output: 10 9 8 7 6 5 4 3 2 1

def printNumber(N):
    if N <= 0:
        return
    
    print(N)
    printNumber(N-1,end = " ")
    
printNumber(10)