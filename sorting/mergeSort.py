# Merge sort
# Given an array arr[], its starting position l and its ending position r. 
# Sort the array using the merge sort algorithm.
# Link - https://www.geeksforgeeks.org/problems/merge-sort/1

arr = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]

def merge(arr, low, mid, high):
    temp = []
    
    i = low
    j = mid + 1
    
    # Merge the two sorted subarrays
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    # Copy remaining elements from the left subarray, if any
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    # Copy remaining elements from the right subarray, if any
    while j <= high:
        temp.append(arr[j])
        j += 1
        
    # Copy the sorted elements back to the original array
    for k in range(low, high + 1):
        arr[k] = temp[k - low]
        
def mergeSort(arr, low, high):
    # Base case: single element is already sorted
    if low < high:
        mid = (low + high) // 2
        
        # Recursively sort the left and right halves
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        
        # Merge the sorted halves
        merge(arr, low, mid, high)
    
    return arr

arr = [2, 1, 5, 3, 4]
n = len(arr)
result = mergeSort(arr, 0, n - 1)
print(result)
