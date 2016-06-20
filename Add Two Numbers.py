# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        add = 0
        while True:
        	if l1 is None and l2 is None and add==0:
        		break
        	if l1 is None:
        		digit1 = 0
        	else:
        		digit1 = l1.val
        		l1 = l1.next
        	if l2 is None:
        		digit2 = 0
        	else:
        		digit2 = l2.val
        		l2 = l2.next
        	
        	tem = digit1 + digit2 + add 
        	add = tem/10
        	ans.append(tem%10)
        return ans 