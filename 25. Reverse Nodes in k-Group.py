# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if k <= 1 or head is None or head.next is None:
			return head
		first = True # record tag, for new head
		ret = head # if not reversed, return head
		pos1 = head # record last k's tail
		next_pos1 = head # record next pos1
		now1 = head.next # pos 1 position ahead now2
		now2 = head # use for trace back
		cnt = 2 # count how many steps have been through
		while True:  
			# print now1.val, now2.val, 'now'
			tmp = now1.next # record the node next to now1
			# print tmp.val, next_pos1.val, 'tmp, next_pos'
			now1.next = now2 # reverse the adjacent nodes
			if cnt == k:
				pos2 = now1 # record the new k's head
				if first:
					ret = now1
					first = False
				else:
					pos1.next = pos2 # last k's tail, next to new k's head
					pos1 = next_pos1 # only when first k has been through, pos1 will start update
				next_pos1 = tmp
				if tmp is None:
					# print next_pos1.val
					# next_pos1 = None
					pos1.next = None
					break
				elif tmp.next is None:
					pos1.next = tmp
					break
				now1 = tmp.next # move to the 2th of new k's
				now2 = tmp # move to the 1th of new k's
				cnt = 2
			else:
				if tmp is not None: # None is not False
					now2 = now1
					now1 = tmp
					cnt += 1 # 1 step further
				else:
					# print now1.val, now2.val
					now1.next = None
					while cnt>2:
						cnt -= 1
						tmp = now2.next
						now2.next = now1 # re reverse the adjacent nodes
						now1 = now2 # step back
						now2 = tmp
						# print now1.val, now2.val
					if pos1 != now2:
						pos1.next = now2 # last k's tail next to the head
					break
		now = ret
		# while now:
		#     print now.val, 
		#     now = now.next
		# print
		return ret