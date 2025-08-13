# Construct Binary Search Tree from Preorder Traversal
# Link - https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

# Example:
# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Example:
# Input: preorder = [1,3]
# Output: [1,null,3]

# Method - Brute force
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        
        # Helper function to insert a value into BST
        def insert(root, val):
            if val < root.val:
                if root.left:
                    insert(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    insert(root.right, val)
                else:
                    root.right = TreeNode(val)

        # Construct BST
        root = TreeNode(preorder[0])
        for val in preorder[1:]:
            insert(root, val)
        
        return root
        
# TC = 0(N)*N
# SC = 0(1)

# Method2 - better approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        inorder = sorted(preorder)  # BST's inorder is always sorted preorder
        
        # Map values to their indices in inorder for O(1) lookup
        idx_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = [0]  # use list to make it mutable in nested scope

        def build_tree(left, right):
            if left > right:
                return None
            
            root_val = preorder[pre_idx[0]]
            root = TreeNode(root_val)
            index = idx_map[root_val]

            pre_idx[0] += 1
            root.left = build_tree(left, index - 1)
            root.right = build_tree(index + 1, right)

            return root

        return build_tree(0, len(preorder) - 1)
    
# TC = 0(NlogN) + o(N)
# SC = 0(N)

# Method3 - optimise way
# Idea:
# In preorder: root is visited first, then left subtree, then right subtree.
# So, we can build the tree recursively by:
# Taking the current value as root.
# All subsequent values smaller than current root are part of the left subtree.
# The rest (greater) are part of the right subtree.
# Use an upper bound to know when to stop recursing.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        self.index = 0

        def helper(bound=float('inf')):
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None
            
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)
            root.left = helper(root_val)     # Left subtree has upper bound = root_val
            root.right = helper(bound)       # Right subtree has upper bound = inherited bound

            return root

        return helper()
    
# TC = 0(N)
# SC = 0(N)
  