# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ret = None
        pos = head
        while pos is not None:
        	if pos.val == val:
        		pos = pos.next
        	else:
        		ret = pos
        		break
        if ret is None:
        	return None
        pos1 = ret 
        pos2 = pos1.next
        while pos2 is not None:
        	if pos2.val == val:
        		pos1.next = pos2.next
        	else:
        		pos1 = pos1.next
        	pos2 = pos2.next
        return ret 