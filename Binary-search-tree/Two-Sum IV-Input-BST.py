# Two Sum IV - Input is a BST
# Link - https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root, k: int) -> bool:
        def dfs(root,seen):
            if root == None:
                return False
            comp = k - root.val
            if comp in seen:
                return True
            seen.add(root.val)
            return dfs(root.left,seen) or dfs(root.right,seen)
        return dfs(root,set())
        