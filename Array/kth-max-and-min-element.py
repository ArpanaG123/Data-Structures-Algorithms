# Find the "Kth" max and min element of an array.
# Link - https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

arr = [7, 10, 4, 3, 20, 15]
k = 3
# Output:  7,10
# Explanation: 3rd smallest element in the given array is 7 and 3rd largest element is 10.


# Merhod1
arr = [7, 10, 4, 3, 20, 15]
k = 3

arr.sort()
# print(arr)
n = len(arr)

print("kth smallest element is: ",arr[k-1])
print("kth largest element is: ",arr[-k])

# TC = 0(nLog n)
# SC = 0(1)

# Method2
arr = [7, 10, 4, 3, 20, 15]
k = 3

def partition_algo(arr, l, r):
    p = arr[l]  # Choose the pivot as the first element
    i = l + 1  # Start from the element next to pivot
    j = r

    while i <= j:
        if arr[i] > p and arr[j] < p:  # We need to swap elements
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        if arr[i] <= p:  # Move i to the right
            i += 1
        if arr[j] >= p:  # Move j to the left
            j -= 1

    arr[l], arr[j] = arr[j], arr[l]  # Place pivot in the correct position
    return j

def quickselect(arr, l, r, k):
    while l <= r:
        pivot_idx = partition_algo(arr, l, r)
        
        if pivot_idx == k - 1:  # Found the k-th smallest
            return arr[pivot_idx]
        elif pivot_idx > k - 1:  # k-th smallest is in the left part
            r = pivot_idx - 1
        else:  # k-th smallest is in the right part
            l = pivot_idx + 1

def kthSmallest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k)

def kthLargest(arr, k):
    n = len(arr)
    return quickselect(arr, 0, n - 1, n - k + 1)

# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3

kth_smallest = kthSmallest(arr, k)
kth_largest = kthLargest(arr, k)

print(f"{k}-th smallest element: {kth_smallest}")  # Expected output: 7 (3rd smallest element)
print(f"{k}-th largest element: {kth_largest}")    # Expected output: 10 (3rd largest element)

# TC = 0(N^2) worst case
# SC = 0(1)

