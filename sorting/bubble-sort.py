# Bubble sort
# Practice Link - https://www.geeksforgeeks.org/problems/bubble-sort/1

arr = [4,3,5,7,2,1]

n = len(arr)

for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)