# Basic - Binary Trees
# Binary Tree allow hirearchical organisation and structire of multilevel sequence.
# Binary tree consist of root node,child node and leaf node.

# Root node - the topmost node of binary tree from which all other node stem out.
# Child node - It is directly connected to a parent node.In BT, a parent can have zero,one or teo children.
# Leaf node - The node that do not have any children.

# Types of Binary Tree
# 1.Full BT
# 2.Complete BT
# 3.Perfect BT
# 4.Balanced BT
# 5.Degenerate Tree

# Binary Tree representation 

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

# Create the root node
root = TreeNode(1)

# Manually add child nodes
root.left = TreeNode(2)
root.right = TreeNode(3)

# Add children to the left child of root
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Add children to the right child of root
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Binary tree traversal
# BFS(Level order traversal)
# DFS(Inorder + preorder + postOrder traversal)