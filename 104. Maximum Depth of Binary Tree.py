# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        ret = 0
        queue = deque()
        if root is not None:
            queue.append((root, 1))
        while len(queue) > 0:
            top, level = queue.popleft()
            ret = max(ret, level)
            if top.left is not None:
                queue.append((top.left, level+1))
            if top.right is not None:
                queue.append((top.right, level+1))
        return ret

        
