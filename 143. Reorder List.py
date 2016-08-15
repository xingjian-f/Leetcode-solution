# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
        	return
        pos = head
        rec = []
        while pos is not None:
        	rec.append(pos)
        	pos = pos.next
        last = None
        tail = None
        for i in range(len(rec)/2):
        	if last is not None:
        		last.next = rec[i]
        	x = rec[i]
        	x.next = rec[-i-1]
        	last = rec[-i-1]
        	tail = rec[-i-1]
        if len(rec)%2==1:
        	last.next = rec[len(rec)/2]
        	tail = rec[len(rec)/2]
        tail.next = None 