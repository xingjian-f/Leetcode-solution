class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        vis = set()
        while True:
        	# print n
        	if n == 1:
        		return True
        	else:
        		tem = str(n)
        		n = 0
        		for i in tem:
        			n += int(i)**2
        		if n in vis:
        			return False
        		else:
        			vis.add(n)
for i in range(100):
	print i, Solution().isHappy(i)