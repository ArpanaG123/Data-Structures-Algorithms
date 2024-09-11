# Linear search

# Link - https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=who-will-win

# Example1:
# Input:
N = 5
K = 6
arr = [1,2,3,4,6]
# Output: 1
# Exlpanation: Since, 6 is present in 
# the array at index 4 (0-based indexing),
# output is 1.
 

# Example2:
# Input:
N = 5
K = 2
arr = [1,3,4,5,6]
# Output: -1
# Exlpanation: Since, 2 is not present 
# in the array, output is -1.

def searchInSorted(arr, N, K):
    #Your code here
        
    for i in range(0,N):
        if arr[i] == K:
            return 1
    return -1

result = searchInSorted(arr,N,K)
print(result)