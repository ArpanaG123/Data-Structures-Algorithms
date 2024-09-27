# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/


# Example 1:
nums1 = [1,3]
nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
nums1 = [1,2]
nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Brute force
def findMedianSortedArrays(arr1,arr2):
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
    
    ans = arr1+arr2
    print(ans)
    
    n1 = len(ans)
    
    if n1 % 2 == 1:
        return ans[n1//2]
    else:
        return (ans[n1 // 2] + ans[n1 // 2 - 1]) / 2

arr1 = [1,3,4,7,10,12]    
arr2 = [2,3,6,15]
res = findMedianSortedArrays(arr1,arr2)
print(res)

# Optimal Approach

arr1 = [1,3,4,7,10,12]    
arr2 = [2,3,6,15]

n1 = len(arr1)
n2 = len(arr2)

n = n1 + n2

i = 0
j = 0

cnt = 0

idx2 = n//2
idx1 = idx2 - 1

ele1 = -1
ele2 = -1

while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        if cnt == idx1:
            ele1 = arr1[i]
        if cnt == idx2:
            ele2 = arr1[i]
        i += 1
        cnt += 1
    else:
        if cnt == idx1:
            ele1 = arr2[j]
        if cnt == idx2:
            ele2 = arr2[j]
        j += 1
        cnt += 1

while i < n1:
    if cnt == idx1:
        ele1 = arr1[i]
    if cnt == idx2:
        ele2 = arr2[i]
    i += 1
    cnt += 1

while j < n2:
    if cnt == idx1:
        ele1 = arr2[j]
    if cnt == idx2:
        ele2 = arr2[j]
    
    j += 1
    cnt += 1

if n % 2 == 1:
    print(ele2)
else:
    print((ele1 + ele2)/2)

