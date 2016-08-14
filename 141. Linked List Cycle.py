# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
        	return False
        pos = head
        next_pos = pos.next
        while True:
        	if next_pos is None:
        		return False
        	next_next_pos = next_pos.next
        	next_pos.next = pos  
        	pos = next_pos
        	next_pos = next_next_pos
        	if pos == head:
        		return True