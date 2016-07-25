# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return head
        vis = set([head.val])
        pos = head.next
        head.next = None
        last = head
        while pos is not None:
        	tmp = pos.next
        	if pos.val not in vis:
        		last.next = pos
        		vis.add(pos.val)
        		last = pos
        		tmp = pos.next
        		pos.next = None
        	pos = tmp
        return head