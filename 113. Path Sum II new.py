# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS([], root, sum)
        return self.res
        
    def DFS(self, path, root, sum):
        if not root:
            return
        if not root.left and not root.right:
            if sum == root.val:
                path += [root.val]
                self.res += [path[:]]
                path.pop()
        path += [root.val]
        self.DFS(path, root.left, sum - root.val)
        self.DFS(path, root.right, sum - root.val)
        path.pop()
