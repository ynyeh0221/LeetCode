# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.res = []
        self.preorder([], root)
        return self.res
        
    def preorder(self, path, root):
        if not root:
            return
        if not root.left and not root.right:
            self.res += ["->".join(path + [str(root.val)])]
        self.preorder(path + [str(root.val)], root.left)
        self.preorder(path + [str(root.val)], root.right)
