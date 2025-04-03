# Top View of Binary Tree
# Link - https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

# You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

# Note: 
# Return the nodes from the leftmost node to the rightmost node.
# If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only. 

# Examples:
# Input: root[] = [1, 2, 3] 
# Output: [2, 1, 3]


from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        if root is None:
            return []
        
        q = deque()
        q.append((root,0))
        
        hd_map = {}
        
        while q:
            node,hd = q.popleft()
            
            if hd not in hd_map:
                hd_map[hd] = node.data
            
            # Traverse left and right with updated horizontal distances
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        # Sort dictionary by horizontal distance and return values
        return [hd_map[key] for key in sorted(hd_map.keys())]
                