# Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        
        ans = []

        q = deque()
        q.append(root)

        flag = True

        while q:
            level_size = len(q)
            current_level = deque()
            
            for _ in range(level_size):
                node = q.popleft()
                
                if flag:
                    current_level.append(node.val)  # append to the right
                else:
                    current_level.appendleft(node.val)  # append to the left  (reversing order)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(list(current_level))
            flag = not flag  # flip the flag for zigzag behavior
        
        return ans

# Time Complexity:

# Processing each node:
# We visit each node exactly once during the breadth-first traversal. For each node, we perform constant-time operations (append to current_level, check left and right children).
# If there are N nodes in the binary tree, the total time spent processing the nodes is O(N).

# Deque operations:
# At each level, we either append to the right or append to the left in the deque. Both append and appendleft operations for a deque are O(1) operations.
# Therefore, processing each level also takes linear time proportional to the number of nodes in that level. Since each node is processed once, this contributes O(N).

# Overall Time Complexity:
# The total time complexity is O(N), where N is the number of nodes in the tree.

# SC = 0(N)
# TC = 0(N)