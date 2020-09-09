# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.c = 0
        self.inorder(root, '')
        return self.c
    def inorder(self, node, stack):
        if not node:
            return
        stack += str(node.val)
        self.inorder(node.left, stack )
        self.inorder(node.right, stack)
        if node.left is None and node.right is None:
            self.c += int(stack, 2)