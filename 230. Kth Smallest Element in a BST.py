# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.k = k
        self.inorder(root)
        return self.res
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.inorder(root.right)
