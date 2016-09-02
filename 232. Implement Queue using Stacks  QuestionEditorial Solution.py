class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.con = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.con.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.con.popleft()


    def peek(self):
        """
        :rtype: int
        """
        return self.con[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.con) == 0