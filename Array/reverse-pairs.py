# Reverse Pairs
# Link - https://leetcode.com/problems/reverse-pairs/description/


# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:
# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1