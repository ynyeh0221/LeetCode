# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = self.lheight(root) + 1
        r = self.rheight(root) + 1
        if l == r:
            return 2 ** l - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
    def lheight(self, root):
        count = 0
        while root.left:
            root = root.left
            count += 1
        return count
    
    def rheight(self, root):
        count = 0
        while root.right:
            root = root.right
            count += 1
        return count
