# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        def inorder(root):
            a = []
            if root.left is not None:
                a.extend(inorder(root.left))
            a.append(root.val)
            if root.right is not None:
                a.extend(inorder(root.right))
            return a
        
        def merge(e):
            a = []
            i = 0
            j = 0
            while i < len(e[0]) and j < len(e[1]):
                if e[0][i] > e[1][j]:
                    a.append(e[1][j])
                    j+=1
                else:
                    a.append(e[0][i])
                    i+=1
            while i < len(e[0]):
                a.append(e[0][i])
                i+=1
            while j < len(e[1]):
                a.append(e[1][j])
                j+=1
            return a
        
        e = []
        for root in [root1, root2]:
            if root:
                e.append(inorder(root))
            else:
                e.append([])
        # print(e)
        return merge(e)
                