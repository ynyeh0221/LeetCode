# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return
        ind = inorder.index(preorder[0])
        root = TreeNode(inorder[ind])
        preorder.pop(0)
        leftin = inorder[:ind]
        rightin = inorder[ind+1:]
        root.left = self.buildTree(preorder, leftin)
        root.right = self.buildTree(preorder, rightin)
        return root
