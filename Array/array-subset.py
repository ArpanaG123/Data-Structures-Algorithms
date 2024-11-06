# Array Subset
# Link - https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1


# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m, where both arrays may contain duplicate elements. The task is to determine whether array a2 is a subset of array a1. It's important to note that both arrays can be sorted or unsorted. Additionally, each occurrence of a duplicate element within an array is considered as a separate element of the set.
a1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]

# Output:Yes
# Explanation:a2[] is a subset of a1[]

# using two pointer

def isSubset(a1,a2,n,m):
    a1.sort()
    a2.sort()
    
    i = 0
    j = 0
    
    while i < n and j < m:
        if a1[i] == a2[j]:
            j += 1
        i += 1
    
    if j == m:
        return "Yes"
    else:
        return "No"
        
a1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]
n = 8
m = 5
result = isSubset(a1,a2,n,m)
print(result)