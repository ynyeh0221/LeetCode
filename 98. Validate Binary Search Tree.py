# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root, -sys.maxint, sys.maxint)
        
    def check(self, root, lower, upper):
        return root.val < upper and root.val > lower and (self.check(root.left, lower, root.val) if root.left else True) and (self.check(root.right, root.val, upper) if root.right else True)
