# Print 1 to N using recursion

# Link - https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1

# Print 1 To N Without Loop
# Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes N as parameter and prints number from 1 to N recursively.
# Don't print newline, it will be added by the driver code.


n = 10
# Output: 1 2 3 4 5 6 7 8 9 10

def printNumber(N):
    if N <= 0:
        return
    
    printNumber(N-1)
    print(N,end = " ")
    
printNumber(10)