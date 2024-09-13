# Next Permutation.
# Link - https://leetcode.com/problems/next-permutation/description/

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

nums = [1,2,3]
# Output: [1,3,2]

# Better using builtin function

# Optimal approach

def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break

        if idx == -1:
            nums.reverse()
            return nums
        
        for i in range(n-1,-1,-1):
            if nums[i] > nums[idx]:
                nums[i],nums[idx] = nums[idx],nums[i]
                break
        
        nums[idx+1:n] = reversed(nums[idx+1:n])
        return nums

# TC = 0(N)
# SC = 0(1)