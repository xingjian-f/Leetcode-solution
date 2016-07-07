# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        now = head
        while now is not None:
        	length += 1
        	now = now.next
        if length == 0 or k%length==0:
        	return head
        k = k%length

        posl = head
        cnt = 0
        posr = head
        last_posl = head
        while cnt < k-1:
        	posr = posr.next
        	cnt += 1

        while posr.next is not None:
        	posr = posr.next
        	last_posl = posl 
        	posl = posl.next

        ret = posl
        last_posl.next = None
        posr.next = head
        return ret  