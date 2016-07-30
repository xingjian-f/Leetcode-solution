# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
        	pos2 = head
        	cnt = 1
        	while cnt < n:
        		pos2 = pos2.next
        		cnt += 1

        	pos2_next = pos2.next
        	pos = head
        	pos_next = pos.next
        	cnt = 1
        	while cnt < n:
        		print pos.val, pos_next.val
        		tmp = pos_next.next
        		pos_next.next = pos 
        		pos = pos_next
        		pos_next = tmp
        		cnt += 1
        	head.next = pos2_next
        	return pos2
        else:
        	pos1_left = head
        	pos2 = head
        	cnt = 1
        	while cnt < m-1:
        		pos1_left = pos1_left.next 
        		cnt += 1
        	cnt = 1
        	while cnt < n:
        		pos2 = pos2.next 
        		cnt += 1

        	pos1 = pos1_left.next 
        	pos1_left.next = pos2 
        	pos2_right = pos2.next 
        	pos = pos1 
        	pos_next = pos.next 
        	cnt = 1
        	while cnt <= n-m:
        		tmp = pos_next.next
        		pos_next.next = pos 
        		pos = pos_next
        		pos_next = tmp
        		cnt += 1
        	pos1.next = pos2_right
        	return head
"""
[5,4,3,2,1]
1 
3
[5,4,3,2,1]
1
5
[5,4,3,2,1]
2
3
[5,4,3,2,1]
2
5
[5,4,3,2,1]
3
4
[5,4,3,2,1]
3
5
"""