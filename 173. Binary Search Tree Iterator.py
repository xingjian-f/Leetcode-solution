# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def move_left(self, node, stack):
        while node.left is not None:
            stack.append(node)
            node = node.left 
        return node


    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            self.exit_next = False
            return
        self.exit_next = True
        self.path_stack = []
        self.now = self.move_left(root, self.path_stack)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.exit_next


    def next(self):
        """
        :rtype: int
        """
        ret = self.now.val
        node = self.now
        if node.right is None:
            if len(self.path_stack) == 0:
                self.exit_next = False
            else:
                node = self.path_stack.pop()
        else:
            node = self.move_left(node.right, self.path_stack)
        self.now = node
        return ret

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())