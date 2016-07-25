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
        cnt = {}
        pos = head
        while pos is not None:
        	cnt[pos.val] = cnt.get(pos.val, 0) + 1
        	pos = pos.next

        pos = head
        while pos is not None and cnt[pos.val] > 1:
        	pos = pos.next
        head = pos
        if head is None:
        	return head

        last = head
        pos = head.next
        last.next = None
        while pos is not None:
        	print pos.val
        	tmp = pos.next
        	if cnt[pos.val] == 1:
        		last.next = pos
        		last = pos
        		last.next = None
        	pos = tmp
        return head