#  Merge Sorted Array
# Link - https://leetcode.com/problems/merge-sorted-array/description/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Type1
# Brute force
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]

n = len(arr1)
m = len(arr2)

i = 0
j = 0

arr3 = [0]*(n+m)
idx = 0

while i < n and j < m:
    if arr1[i] <= arr2[j]:
        arr3[idx] = arr1[i]
        idx += 1
        i += 1
    else:
        arr3[idx] = arr2[j]
        idx += 1
        j += 1

while i < n:
    arr3[idx] = arr1[i]
    i += 1
    idx += 1

while j < m:
    arr3[idx] = arr2[j]
    j += 1
    idx += 1
    
for i in range(0,n+m):
    if i < n:
        arr1[i] = arr3[i]
    else:
        arr2[i-n] = arr3[i]
print(arr1 + arr2)

# TC = 0(N+M) + 0(N+M)
# SC = 0(N+M)

# Better

arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]

n = len(arr1)
m = len(arr2)

i = n-1
j = 0

while i >= 0  and j < m:
    if arr1[i] > arr2[j]:
        arr1[i],arr2[j] = arr2[j],arr1[i]
        i -= 1
        j += 1
    else:
        break

arr1.sort()
arr2.sort()

print(arr1 + arr2)

# TC = 0(min(n,m)) + 0(nlogn) + 0(mlogm)
# SC = 0(1)

# Type2 - 
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

def merge(nums1,m,nums2,n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Pointers for nums1, nums2, and the end of the merged array
    i = m - 1  # Last element of the first part of nums1
    j = n - 1  # Last element of nums2
    k = m + n - 1  # Last element of nums1

    # Merge nums1 and nums2 from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Optimal approach - using gap method

def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def merge(arr1, arr2, n, m):
    # len of the imaginary single array:
    len = n + m

    # Initial gap:
    gap = (len // 2) + (len % 2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < len:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)

arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n = len(arr1)
m = len(arr2)
merge(arr1, arr2, n, m)
print(arr1+arr2)
