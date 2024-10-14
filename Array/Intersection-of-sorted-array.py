# Find the Intersection of the two arrays.
# Link - https://www.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1
# Link2 - https://leetcode.com/problems/intersection-of-two-arrays/description/

# Input:
a = [1, 2, 3, 4, 5, 6]
b = [3, 4, 5, 6, 7]

# Output: 1

# Method1
res = []

for i in a:
    if i not in res and i in b:
        res.append(i)

print(res)
print(len(res))

# Time Complexity
# Outer Loop: Runs 0(N), 
# Membership Check (i not in res): Takes 0(k) where,k is the length of res.
# Membership Check (i in b): Takes  0(M) where,m is the length of array b.
# So, the total time complexity is 0(N*K*M)
# In the worst case, if both res and b are large, this can result in very slow performance, especially when the input arrays are long.

# Method2 - Optimized Code Using Sets

a = [89, 24, 75, 11, 23]
b = [89, 2, 4]

set1 = set(b)
intersection = set()

for i in a:
    if i in set1:
        intersection.add(i)
print(intersection)
print(len(intersection))

# Type2 
# Input: 
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Type2
nums1 = [1,2,2,1]
nums2 = [2,2]
freq = {}
res = []

for i in nums1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in nums2:
    if i in freq and freq[i] > 0:
        res.append(i)
        freq[i] -= 1
        
print(res)
print(len(res))

# Intersection of two sorted arrays

arr1 = [1, 2, 2, 3, 3, 4, 5, 6]
arr2 = [2, 3, 3, 5, 6, 6, 7]

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0

ans = []
while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        ans.append(arr1[i])
        i += 1
        j += 1

print(ans)

# TC = 0(N1+N2)
# SC = 0(1)

# using two pointer for unique elements only
# leetcode - 349
def intersection(nums1,nums2):
    nums1.sort()
    nums2.sort()
        
    n = len(nums1)
    m  = len(nums2)

    i = 0
    j = 0

    ans = []
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            if not ans or ans[-1] != nums1[i]:
                ans.append(nums1[i])
            i += 1
            j += 1

    return ans

nums1 = [1,2,2,1]
nums2 = [2,2]
# Output: [2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# Output: [9,4]

result = intersection(nums1,nums2)
print(result)