# Binary Tree Preorder Traversal
# Link - https://leetcode.com/problems/binary-tree-preorder-traversal/description/


# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# root = [1,null,2,3]
# Output: [1,2,3]

# Recursive Approach
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
# TC = 0(N)
# SC = 0(N)

# Iterative Approach
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        preorder = []

        if root is None:
            return []
        st = []
        st.append(root)

        while len(st) != 0:
            root = st.pop()
            preorder.append(root.val)

            if root.right:
                st.append(root.right)

            if root.left:
                st.append(root.left)
        return preorder
