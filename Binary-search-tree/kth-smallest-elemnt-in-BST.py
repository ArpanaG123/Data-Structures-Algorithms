# Kth Smallest Element in a BST
# link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            # Traverse left, root, then right
            return inorder(node.left) + [node.val] + inorder(node.right)

        sorted_nodes = inorder(root)
        return sorted_nodes[k - 1]


