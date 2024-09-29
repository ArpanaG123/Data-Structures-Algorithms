# Print name

# Link - https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times

# Print GFG n times without the loop.

# Input:5
# Output:GFG GFG GFG GFG GFG


# Code - using recursion
def printName(N):
    if N <= 0:
        return
    
    print("ARPANA",end = " ")
    printName(N-1)

printName(5)