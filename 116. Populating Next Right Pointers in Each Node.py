# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.DFS(root)
    
    def DFS(self, root):
        if not root or (not root.left and not root.right):
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        else:
            root.right.next = None
        self.DFS(root.left)
        self.DFS(root.right)
