# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        ind = inorder.index(postorder[len(postorder)-1])
        postorder.pop()
        root = TreeNode(inorder[ind])
        left = inorder[:ind]
        right = inorder[ind+1:]
        root.right = self.buildTree(right, postorder)
        root.left = self.buildTree(left, postorder)
        return root
