# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.minheight = sys.maxint
        self.DFS(root, 0)
        return self.minheight
        
    def DFS(self, root, height):
        if not root:
            return
        if not root.left and not root.right:
            if height + 1 < self.minheight:
                self.minheight = height + 1
            return
        height += 1
        self.DFS(root.left, height)
        self.DFS(root.right, height)
