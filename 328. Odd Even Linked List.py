# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_tail = None
        even_head = None
        odd_tail = None
        odd_head = None
        pos = head
        cnt = 1
        while pos is not None:
        	if cnt == 1:
        		if odd_tail is None:
        			odd_head = pos
        		else:
        			odd_tail.next = pos
        		odd_tail = pos
        		cnt = 0
        	else:
        		if even_tail is None:
        			even_head = pos
        		else:
        			even_tail.next = pos
        		even_tail = pos
        		cnt = 1
        	pos = pos.next
        if odd_tail is not None:
        	odd_tail.next = even_head
        if even_tail is not None:
        	even_tail.next = None
        return odd_head