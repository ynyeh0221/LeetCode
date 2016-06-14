# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        self.res = False
        self.DFS(root, sum)
        return self.res
    
    def DFS(self, root, sum):
        if root == None:
            return
        if root.left == None and root.right == None:
            if sum == root.val:
                self.res = True
        self.DFS(root.left, sum - root.val)
        self.DFS(root.right, sum - root.val)
