# Binary Tree Right Side View
# Link - https://leetcode.com/problems/binary-tree-right-side-view/description/

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        result = []
        q = deque([root])
        
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                
                # If it's the last node at this level, add to result
                if i == n - 1:
                    result.append(node.val)
                
                # Add left and right children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return result
    
# TC = 0(N)
# SC = 0(N)