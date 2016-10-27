# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level = []
        from collections import deque
        q = deque([])
        last = 0
        if root is not None:
            q.append((root, 0))
        while len(q) > 0:
            top = q.popleft()
            node, now = top
            if now > last:
                last = now
                for i in range(len(level)-1):
                    level[i].next = level[i+1]
                level[-1].next = None
                level = []
            level.append(node)
            if node.left is not None:
                q.append((node.left, now+1))
            if node.right is not None:
                q.append((node.right, now+1))

        if len(level) > 0:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None


# Solution().connect(TreeLinkNode)
