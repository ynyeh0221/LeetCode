# memory exceed

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
        if len(preorder) == 0:
            return []
        root = TreeNode(preorder[0])
        leftin = inorder[:inorder.index(preorder[0])]
        rightin = inorder[inorder.index(preorder[0])+1:]
        leftpre = preorder[1:1+len(leftin)]
        rightpre = preorder[1+len(leftin):len(preorder)]
        root.left = self.build(leftpre, leftin)
        root.right = self.build(rightpre, rightin)
        return root
        
    def build(self, preorder, inorder):
        if len(preorder) == 0:
            return
        root = TreeNode(preorder[0])
        leftin = inorder[:inorder.index(preorder[0])]
        rightin = inorder[inorder.index(preorder[0])+1:]
        leftpre = preorder[1:1+len(leftin)]
        rightpre = preorder[1+len(leftin):len(preorder)]
        root.left = self.build(leftpre, leftin)
        root.right = self.build(rightpre, rightin)
        return root
