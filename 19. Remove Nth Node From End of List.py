# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        pos = head
        while pos:
        	length += 1
        	pos = pos.next
        cnt = length-n
        print cnt
        if cnt == 0:
        	return head.next
        pos = head
        while True:
        	cnt -= 1
        	if cnt == 0:
        		pos.next = pos.next.next
        		break
        	pos = pos.next
        	
        return head