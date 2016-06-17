# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        
        while len(queue) > 0:
            current = queue.pop(0)
            curr_node, curr_level = current[0], current[1]
            res[len(res) - 1] += [curr_node.val]
            if curr_node.left:
                queue += [(curr_node.left, curr_level + 1)]
            if curr_node.right:
                queue += [(curr_node.right, curr_level + 1)]
            if len(queue) > 0 and queue[0][1] > curr_level:
                res += [[]]
        return res
