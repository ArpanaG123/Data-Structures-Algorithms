# Binary Tree Maximum Path Sum
# Link - https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathDown(self,node,maxi):
        if node is None:
            return 0
        left_sum = max(0,self.maxPathDown(node.left,maxi))
        right_sum = max(0,self.maxPathDown(node.right,maxi))

        maxi[0] = max(maxi[0], left_sum + right_sum + node.val)

        return max(left_sum,right_sum) + node.val

    def maxPathSum(self, root) -> int:
        maxi = [float('-inf')]

        self.maxPathDown(root,maxi)
        return maxi[0]