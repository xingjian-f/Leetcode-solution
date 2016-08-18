# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1 = 0
        len2 = 0
        pos1 = headA
        pos2 = headB
        while pos1 is not None:
        	len1 += 1
        	pos1 = pos1.next
        while pos2 is not None:
        	len2 += 1
        	pos2 = pos2.next

        if len1 > len2:
        	headA, headB = headB, headA
        cnt = abs(len1-len2)
        pos1 = headA
        pos2 = headB
        while cnt > 0:
        	pos2 = pos2.next
        	cnt -= 1
        while pos1 is not None and pos2 is not None:
        	if pos1 == pos2:
        		return pos1
        	pos1 = pos1.next
        	pos2 = pos2.next
        return None