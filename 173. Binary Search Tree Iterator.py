# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nums = []
        self.stack = [root]
        if not root:
            return
        while self.stack:
            while root:
                self.stack += [root]
                root = root.left
            root = self.stack.pop()
            self.nums += [root.val]
            root = root.right

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.nums) > 1 else False

    def next(self):
        """
        :rtype: int
        """
        return self.nums.pop(0)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
