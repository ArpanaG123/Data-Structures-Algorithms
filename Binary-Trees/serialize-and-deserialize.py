# Serialize and Deserialize Binary Tree
# Link - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Examples:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Definition for a binary tree node.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        vals = []
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        vals = iter(data.split(','))
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))