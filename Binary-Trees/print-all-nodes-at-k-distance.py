# All Nodes Distance K in Binary Tree
# Link - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/


# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# You can return the answer in any order.

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def markParent(self, root: TreeNode, parent_map: dict):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        parent_map = {}
        self.markParent(root, parent_map)

        visited = set()
        queue = deque()
        queue.append((target, 0))
        visited.add(target)
        result = []

        while queue:
            current_node, current_distance = queue.popleft()
            if current_distance == k:
                result.append(current_node.val)
            elif current_distance < k:
                for neighbor in [current_node.left, current_node.right, parent_map.get(current_node)]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_distance + 1))
        
        return result
