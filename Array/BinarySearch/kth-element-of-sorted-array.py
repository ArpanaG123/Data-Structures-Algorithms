# K-th element of two Arrays
# Given two sorted arrays arr1 and arr2 and an element k. The task is to find the element that would be at the kth position of the combined sorted array.

k = 5
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
# Output: 6
# Explanation: The final combined sorted array would be - 1, 2, 3, 4, 6, 7, 8, 9, 10. The 5th element of this array is 6.

# Link - https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=k-th-element-of-two-sorted-array

# Brute force

def kthElement(k, arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    i = n1 - 1
    j = 0

    while i >= 0 and j < n2:
        if arr1[i] > arr2[j]:
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i -= 1
            j += 1
        else:
            break

    arr1.sort()
    arr2.sort()

    arr3 = arr1 + arr2
    arr3.sort()

    return arr3[k-1]

arr1 = [100, 112, 256, 349, 770]  
arr2 = [72, 86, 113, 119, 265, 445, 892]
k = 7

ans = kthElement(k, arr1, arr2)
print(ans)
