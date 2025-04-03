# Symmetric Tree
# Link - https://leetcode.com/problems/symmetric-tree/description/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self,left,right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return left.val == right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)

        
    def isSymmetric(self, root) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left,root.right)
