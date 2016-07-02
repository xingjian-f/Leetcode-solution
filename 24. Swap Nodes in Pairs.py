# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		now = head
		if head and head.next:
			ret = head.next
		else:
			ret= head
		while now and now.next:
			pos2 = now.next
			pos3 = pos2.next
			pos4 = None
			if pos3:
				pos4 = pos3.next
			pos2.next = now
			if pos4:
				now.next = pos4
			else:
				now.next = pos3
			now = pos3
		return ret