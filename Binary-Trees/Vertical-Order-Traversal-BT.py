# Vertical Order Traversal of a Binary Tree
# Link - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []

        # Dictionary to store nodes at each (column, row)
        node_map = {}

        # Queue to perform BFS, storing (node, column, row)
        queue = deque([(root, 0, 0)])

        while queue:
            node, col, row = queue.popleft()

            # Add the node's value to the node_map for the given (col, row)
            if col not in node_map:
                node_map[col] = []
            node_map[col].append((row, node.val))

            # Traverse the left subtree with updated column and row
            if node.left:
                queue.append((node.left, col - 1, row + 1))

            # Traverse the right subtree with updated column and row
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        # Sort the columns based on their horizontal distance
        result = []
        for col in sorted(node_map.keys()):
            # Sort the nodes first by row, then by value
            column_nodes = sorted(node_map[col], key=lambda x: (x[0], x[1]))
            result.append([val for row, val in column_nodes])

        return result
  
