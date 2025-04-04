# Same Tree
# Link - https://leetcode.com/problems/same-tree/description/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Definition for a binary tree node.
# Using recursive approach - preorder traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p,q) -> bool:

        if q is None or p is None:
            return p == q
        
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)