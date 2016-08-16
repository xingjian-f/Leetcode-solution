# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
        	return head

        length = 0
        pos = head
        while pos is not None:
        	length += 1
        	pos = pos.next

        mid = head
        cnt = length/2-1
        while cnt > 0:
        	mid = mid.next
        	cnt -= 1

        lhead = head
        rhead = mid.next
        mid.next = None

        left = self.sortList(lhead)
        right = self.sortList(rhead)
        ret = None
        last = None
        while left is not None and right is not None:
        	if left.val < right.val:
        		node = left
        		left = left.next
        	else:
        		node = right
        		right = right.next
        	if ret is None:
        		ret = node 
        		last = node
        	else:
        		last.next = node
        		last = node 
        if left is not None:
        	last.next = left
        elif right is not None:
        	last.next = right

        return ret 