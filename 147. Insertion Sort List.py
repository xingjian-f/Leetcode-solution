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
        while head is not None:
        	tar = head.val
        	tmp_head = head
        	head = head.next
        	if ret is None:
        		ret = tmp_head
        		ret.next = None
        	else:
        		pos = ret
        		last = None 
        		while pos is not None and tar > pos.val:
        			last = pos
        			pos = pos.next
        		if last is None:
        			ret = tmp_head
        		else:
        			last.next = tmp_head
        		tmp_head.next = pos
        return ret