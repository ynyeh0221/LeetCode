# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not (root == None or (root.left==None and root.right == None)):
            self.queue = []
            p = root
            self.preorder(p)
            while len(self.queue) > 0:
                curr = self.queue.pop(0)
                p.right = curr
                p.left = None
                p = p.right
        
    def preorder(self, p):
        if not p:
            return
        self.queue += [p]
        self.preorder(p.left)
        self.preorder(p.right)
