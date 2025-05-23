# Construct Binary Tree from Inorder and Postorder Traversal
# link - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        # Map each value to its index in inorder for quick lookup
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(left,right):
            if left > right:
                return None
            
            # The next root is the last item in postorder
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Build right subtree first (since we're popping from the end)
            index = inorder_index_map[root_val]
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)
        