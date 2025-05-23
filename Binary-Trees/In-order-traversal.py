# Binary Tree Inorder Traversal
# Link - https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
# TC = 0(N)
# SC = 0(N)


# Iterative approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        inorder = []
        st = []
        current = root

        while current or st:
            # Traverse to the leftmost node
            while current:
                st.append(current)  # Push the current node to the stack
                current = current.left

            # Process the node
            current = st.pop()  # Pop the node from the stack
            inorder.append(current.val)  # Append its value to the result

            # Now move to the right subtree
            current = current.right

        return inorder        