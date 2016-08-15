# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret = None
        last = None
        while head is not None:
        	min_pos = head
        	min_pos_left = None
        	min_val = head.val
        	pos1 = head
        	pos2 = head.next
        	while pos2 is not None:
        		if pos2.val < min_val:
        			min_val = pos2.val 
        			min_pos = pos2
        			min_pos_left = pos1
        		pos1 = pos2
        		pos2 = pos2.next
        	if min_pos_left is not None:
        		min_pos_left.next = min_pos.next
        	else:
        		head = min_pos.next

        	if ret is None:
        		ret = min_pos
        		last = min_pos
        	else:
        		last.next = min_pos
        		last = min_pos

        return ret