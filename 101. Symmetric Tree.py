# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        ret = []
        queue = deque()
        now_level = 0
        if root is not None:
            queue.append((root, 1))
        while len(queue) > 0:
            top, level = queue.popleft()
            if top is None:
                val = 'None'
            else:
                val = top.val
            if level == now_level:
                ret[-1].append(val)
            else:
                ret.append([val])
                now_level = level
            if top is None:
                continue
            queue.append((top.left, level+1))
            queue.append((top.right, level+1))
        print ret
        for i in range(1, len(ret)):
            length = len(ret[i])
            if length%2 != 0 or ret[i][:length/2][::-1] != ret[i][length/2:]:
                return False
            
        return True
        