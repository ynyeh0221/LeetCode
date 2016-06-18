# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        if abs(self.height(root.left, 0) - self.height(root.right, 0)) > 1:
            return False
        elif (not self.isBalanced(root.left)) or (not self.isBalanced(root.right)):
            return False
        return True
        
    def height(self, root, h):
        if not root:
            return h
        return max(self.height(root.left, h), self.height(root.right, h)) + 1
