# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
        	return head
        pos1 = head
        pos2 = head.next
        while pos2 is not None:
        	tem = pos2.next
        	pos2.next = pos1
        	pos1 = pos2
        	pos2 = tem
        head.next = None
        return pos1