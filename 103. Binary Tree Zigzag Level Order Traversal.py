# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        stack = []
        while queue:
            node, level = queue.pop(0)
            res[len(res)-1] += [node.val]
            if level % 2 ==0:
                if node.left:
                    stack += [(node.left, level+1)]
                if node.right:
                    stack += [(node.right, level+1)]
            else:
                if node.right:
                    stack += [(node.right, level+1)]
                if node.left:
                    stack += [(node.left, level+1)]
            if not queue and stack:
                while stack:
                    queue += [stack.pop()]
            if  queue and level < queue[0][1]:
                res += [[]]
        return res
