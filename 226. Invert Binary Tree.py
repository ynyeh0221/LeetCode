# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        p = root
        self.invert(p)
        return root
        
    def invert(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert(root.left)
        self.invert(root.right)
