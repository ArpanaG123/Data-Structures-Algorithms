# Count Complete Tree Nodes
# Link - https://leetcode.com/problems/count-complete-tree-nodes/description/

# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 6


# Approach1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0 

    def traverse(self,node):
        if node is None:
            return
        self.cnt += 1
        self.traverse(node.left)
        self.traverse(node.right)
        
    def countNodes(self, root) -> int:
        self.traverse(root)
        return self.cnt
    
# TC = 0(N)
# SC = 0(N)
# Note: This is complete tree so it can be the auxiliary space as 0(logn) and in simple BT SC = 0(N)

# Approach2 : find height of the tree and then 2^height of tree - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeftHeight(self,node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def findRightHeight(self,node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
        
    def countNodes(self, root) -> int:
        if root is None:
            return 0
        lh = self.findLeftHeight(root)
        rh = self.findRightHeight(root)

        if lh == rh:
            # It's a perfect binary tree: number of nodes = 2^height - 1
            return (1 << lh) - 1
        
        # Otherwise, recurse on left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        
# TC = 0(logn)^2
# as logn for traversal and finding height for that logn also so maximum TC will be logn^2
# SC = 0(logN)
        