# Construct Binary Tree from Preorder and Inorder Traversal
# Link - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Examples
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index = {value: idx for idx, value in enumerate(inorder)}
        pre_idx = [0]  # Use list for mutable integer in nested function
        
        def helper(left: int, right: int):
            if left > right:
                return None

            root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1

            root = TreeNode(root_val)
            index = inorder_index[root_val]

            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)
        