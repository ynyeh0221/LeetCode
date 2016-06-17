# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.preorder(0, root)
        return self.res
    
    def preorder(self, path, root):
        if not root:
            return
        if not root.left and not root.right:
            self.res += 10 * path + root.val
        self.preorder(10 * path + root.val, root.left)
        self.preorder(10 * path + root.val, root.right)
