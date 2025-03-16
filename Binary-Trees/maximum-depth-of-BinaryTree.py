# Maximum Depth of Binary Tree
# Link - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return 1 + max(lh,rh)
    
# TC = 0(N)
# SC = 0(N)