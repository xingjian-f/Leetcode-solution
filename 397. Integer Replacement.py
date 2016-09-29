class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        from collections import deque
        queue = deque([(n, 0)])
        while True:
        	val, step = queue.popleft()
        	if val == 1:
        		return step
        	if val%2==0:
        		queue.append((val/2, step+1))
        	else:
        		queue.append((val+1, step+1))
        		queue.append((val-1, step+1))

print Solution().integerReplacement(5000000)