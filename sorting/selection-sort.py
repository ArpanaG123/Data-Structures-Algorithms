# SELECTION SORT

# Pick minimum element and place at first and so on...

arr = [4,3,5,7,2,1]
n = len(arr)

for i in range(0,n):
    min_idx = i
    for j in range(i+1,n):
        if arr[j] < arr[min_idx]:
            arr[j],arr[min_idx] = arr[min_idx],arr[j]
print(arr)

# [1, 2, 3, 4, 5, 7] - output

# TC = 0(N^2)
