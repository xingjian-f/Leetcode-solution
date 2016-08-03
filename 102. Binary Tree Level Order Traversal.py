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
        from collections import deque
        ret = []
        queue = deque()
        now_level = 0
        if root is not None:
            queue.append((root, 1))
        while len(queue) > 0:
            top, level = queue.popleft()
            if level == now_level:
                ret[-1].append(top.val)
            else:
                ret.append([top.val])
                now_level = level
            if top.left is not None:
                queue.append((top.left, level+1))
            if top.right is not None:
                queue.append((top.right, level+1))
        return ret
        