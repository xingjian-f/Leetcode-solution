# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        pos = head
        while pos is not None:
            self.length += 1
            pos = pos.next


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = 1.0 / self.length
        not_chose = 1
        import random 
        pos = self.head
        while pos is not None:
            res = random.random()
            x = p / not_chose
            if res < x:
                return pos.val
            not_chose *= (1 - x)
            pos = pos.next 


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom() 