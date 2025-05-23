# Maximum Width of Binary Tree
# Link - https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if root is None:
            return 0
        
        max_width = 0
        q = deque([(root, 0)])  # queue stores (node, index)

        while q:
            level_length = len(q)
            _, level_head_index = q[0]
            for _ in range(level_length):
                node, idx = q.popleft()
                curr_index = idx - level_head_index  # Normalize index
                if node.left:
                    q.append((node.left, 2 * curr_index))
                if node.right:
                    q.append((node.right, 2 * curr_index + 1))
            # width = last index - first index + 1
            max_width = max(max_width, curr_index + 1)

        return max_width

        
