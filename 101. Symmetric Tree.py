# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        p1, p2 = root, root
        self.symm(p1, p2)
        return self.res
    
    def symm(self, p1, p2):
        if not p1 and not p2:
            return
        elif not p1 and p2:
            self.res = False
            return
        elif p1 and not p2:
            self.res = False
            return
        if p1.val != p2.val:
            self.res = False
        self.symm(p1.left, p2.right)
        self.symm(p1.right, p2.left)
