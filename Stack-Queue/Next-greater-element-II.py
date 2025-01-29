#  Next Greater Element II
# Link - https://leetcode.com/problems/next-greater-element-ii/description/

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.

def nextGreaterElements(nums):
    n = len(nums)
    
    next_greater_element = [0] * n
    
    st = []
    
    for i in range((2*n-1),-1,-1):
        while len(st) != 0 and st[-1] <= nums[i%n]:
            st.pop()
        
        if i < n:
            if len(st) == 0:
                next_greater_element[i] = -1
            else:
                next_greater_element[i] = st[-1]
        
        st.append(nums[i%n])
        
    return next_greater_element

nums = [2,10,12,1,11]
result = nextGreaterElements(nums)
print(result)