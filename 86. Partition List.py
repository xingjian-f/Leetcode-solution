# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
        	return head
        # save all nodes in a new list
        order = []
		# find smaller part 
        pos = head
        while pos is not None:
        	if pos.val < x:
        		order.append(pos)
        	pos = pos.next
        # find larger part
        pos = head
        while pos is not None:
        	if pos.val >= x:
        		order.append(pos)
        	pos = pos.next
        # link them 
        for i in range(len(order)-1):
        	order[i].next = order[i+1]
        order[-1].next = None
        return order[0]