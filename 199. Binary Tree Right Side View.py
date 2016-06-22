# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level = 0
        queue = [(root, level)]
        res = []
        while len(queue) > 0:
            curr = queue.pop(0)
            if len(res) == curr[1]:
                res += [curr[0].val]
            if curr[0].right:
                queue += [(curr[0].right, curr[1]+1)]
            if curr[0].left:
                queue += [(curr[0].left, curr[1]+1)]
        return res
