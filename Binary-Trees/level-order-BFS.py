# Binary Tree Level Order Traversal
# Link - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        ans = []

        if root is None:
            return []
        
        q = deque([root])  # Use a deque as a queue for BFS
        
        while q:
            level_size = len(q)  # Number of nodes at the current level
            current_level = []  # List to store the nodes at this level
            
            for _ in range(level_size):
                node = q.popleft()  #remove the node from the front of the queue
                current_level.append(node.val) #Add the node's value to the curr level
                
                # Add the children of the current node to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(current_level)  # Add the current level to the result
        
        return ans
    
# TC = 0(N)
# SC = 0(N)

# Approach Iterative
class Node:
    def init(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrderTraversal(self,root):
        # code here
        ans = []
        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans

        