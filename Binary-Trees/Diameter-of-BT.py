# Diameter of Binary Tree
# Link - https://leetcode.com/problems/diameter-of-binary-tree/description/


# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


# Approach1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        self.ans = 0

        def heights(node):
            if node is None:
                return 0
        
            left_h = heights(node.left)
            right_h = heights(node.right)

            self.ans = max(self.ans,left_h + right_h) 

            return 1 + max(left_h, right_h) 

        heights(root)
        return self.ans

# Time Complexity: O(N^2) 

# Approach2 - by eliminating extra repeating steps                 
# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to find the diameter of the binary tree
class Solution:
    def diameterOfBinaryTree(self, root):
        # Initialize the variable to store the diameter of the tree
        diameter = [0]
        # Call the height function to traverse the tree and calculate diameter
        self.height(root, diameter)
        # Return the calculated diameter
        return diameter[0]

    # Function to calculate the height of the tree and update the diameter
    def height(self, node, diameter):
        # Base case: If the node is None, return 0 indicating the height of an empty tree
        if not node:
            return 0

        # Recursively calculate the height of left and right subtrees
        lh = self.height(node.left, diameter)
        rh = self.height(node.right, diameter)

        # Update the diameter with the maximum of current diameter or sum of left and right heights
        diameter[0] = max(diameter[0], lh + rh)

        # Return the height of the current node's subtree
        return 1 + max(lh, rh)


# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculate the diameter of the binary tree
    diameter = solution.diameterOfBinaryTree(root)

    print("The diameter of the binary tree is:", diameter)


# Time Complexity: O(N) 