# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if (l2 and l1 and l2.val < l1.val) or l1 is None:
			head = l2
			if l2:
				l2 = l2.next
		else:
			head = l1
			if l1:
				l1 = l1.next
		now = head
		while l1 and l2:
			if l1.val <= l2.val:
				now.next = l1
				now = l1
				l1 = l1.next
			else:
				now.next = l2
				now = l2
				l2 = l2.next
		if l1:
			now.next = l1
		if l2:
			now.next = l2
		return head

	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		# ret = []
		if len(lists) == 0:
			return []
		while len(lists) > 1:
			tmp = []
			if len(lists)%2==1:
				tmp.append(lists[-1])
			for i in range(0,len(lists)-1,2):
				tmp.append(self.mergeTwoLists(lists[i], lists[i+1]))
			lists = tmp
		return lists[0]