# Validate Binary Search Tree
# Link - https://leetcode.com/problems/validate-binary-search-tree/description/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (helper(node.left, min_val, node.val) and
                    helper(node.right, node.val, max_val))
        
        return helper(root, float('-inf'), float('inf'))

# TC = 0(N)
# SC = 0(N)