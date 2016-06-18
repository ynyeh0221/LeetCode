# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or len(stack) > 0:
            while root:
                stack +=[root]
                root = root.left
            root = stack.pop()
            res += [root.val]
            root = root.right
        return res
