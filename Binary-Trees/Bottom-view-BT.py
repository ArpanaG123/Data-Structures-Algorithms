# Bottom View of Binary Tree
# link - https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

# Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

# Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level traversal is considered. For example, in the below diagram, 3 and 4 are both the bottommost nodes at a horizontal distance of 0, here 4 will be considered.

#                       20
#                     /    \
#                   8       22
#                 /   \     /   \
#               5      3 4     25
#                      /    \      
#                  10       14

# For the above tree, the output should be 5 10 4 14 25.

# Examples :
# Input:
#        1
#      /   \
#     3     2
# Output: 3 1 2
# Explanation: First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.
# Thus bottom view of the binary tree will be 3 1 2.

from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        
        hd_map = {}
        
        q = deque()
        q.append((root,0))
        
        while q:
            node,hd = q.popleft()
            
            hd_map[hd] = node.data
            
            if node.left:
                q.append((node.left,hd-1))
            
            if node.right:
                q.append((node.right,hd+1))
        
        return [hd_map[hd] for hd in sorted(hd_map.keys())]