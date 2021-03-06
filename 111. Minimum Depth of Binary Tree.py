# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        ret = 1e9
        queue = deque()
        if root is not None:
            queue.append((root, 1))
        else:
            return 0
        while len(queue) > 0:
            top, level = queue.popleft()
            if top.left is None and top.right is None:
                return level
            if top.left is not None:
                queue.append((top.left, level+1))
            if top.right is not None:
                queue.append((top.right, level+1))
        return ret