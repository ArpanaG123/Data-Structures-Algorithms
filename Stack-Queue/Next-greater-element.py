# Next Greater Element I
# Link - https://leetcode.com/problems/next-greater-element-i/description/

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Type1
# arr = [4,12,5,3,1,2,5,3,1,2,4,6]
# output = [12, -1, 6, 5, 2, 5, 6, 4, 2, 4, 6, -1]

def nextGreaterElement(arr):
    st = []
    n = len(arr)
    next_greater_element = [0]*n
    
    for i in range(n-1,-1,-1):
        while (len(st) != 0 and st[-1] <= arr[i]):
            st.pop()
        
        if len(st) == 0:
            next_greater_element[i] = -1
        else:
            next_greater_element[i] = st[-1]
        st.append(arr[i])
        
    return next_greater_element
    
arr = [4,12,5,3,1,2,5,3,1,2,4,6]
result = nextGreaterElement(arr)
print(result)

# TC = 0(2N)
# sc = 0(N) + 0(N)

# Type2
nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

def nextGreaterElement(nums1,nums2):
    n1 = len(nums1)
    n2 = len(nums2)

    st = []
    next_greater_element = {}

    for i in range(n2-1,-1,-1):
        while len(st) != 0 and st[-1] <= nums2[i]:
            st.pop()
            
        if len(st) == 0:
            next_greater_element[nums2[i]] = -1
        else:
            next_greater_element[nums2[i]] = st[-1]
        st.append(nums2[i])   
        
    result = [next_greater_element[num] for num in nums1]
    return result
    
nums1 = [4,1,2]
nums2 = [1,3,4,2]
result = nextGreaterElement(nums1,nums2)
print(result)