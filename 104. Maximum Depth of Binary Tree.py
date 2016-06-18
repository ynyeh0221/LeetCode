# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.height(root, 0)
    
    def height(self, root, h):
        if not root:
            return h
        return max(self.height(root.left, h), self.height(root.right, h)) + 1
