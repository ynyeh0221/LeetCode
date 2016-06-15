# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        while len(queue) > 0:
            temp = queue.pop(0)
            p = temp[0]
            level = temp[1]
            res[len(res) - 1] += [p.val]
            if p.left:
                queue += [(p.left, level + 1)]
            if p.right:
                queue += [(p.right, level + 1)]
            if len(queue) > 0 and level != queue[0][1]:
                res += [[]]
        return res[::-1]
