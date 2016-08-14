# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return None
        pos1 = head
        pos2 = head
        step = 0
        while True:
        	if pos1.next is None:
        		return None
        	pos1 = pos1.next
        	if pos2.next is None or pos2.next.next is None:
        		return None
        	pos2 = pos2.next.next
        	step += 1
        	if pos1 == pos2:
        		break

        pos1 = head
        pos2 = head
        while step > 0:
        	pos2 = pos2.next
        	step -= 1
        while True:
        	if pos1 == pos2:
        		return pos1
        	pos1 = pos1.next
        	pos2 = pos2.next