# Balanced Binary Tree
# Link - https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Note:
# for every balanced tree = height(left) - height(right) <= 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfsHeight(self,root):
        if root is None:
            return 0
        lh = self.dfsHeight(root.left)
        if lh == -1:
            return -1
        rh = self.dfsHeight(root.right)
        if rh == -1:
            return -1
        
        if abs(lh-rh) > 1:
            return -1
        return max(lh,rh) + 1

    def isBalanced(self, root) -> bool:
        return self.dfsHeight(root) != -1
    
# TC = 0(N)
# SC = 0(N)