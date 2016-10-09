class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # a = range(1, n+1)
        s = 2
        if n == 1:
        	s = 1
        length = n
        step = 2
        tag = 2
        while length/2 > 1:
        	# print length, s, step
        	if tag == 2:
	        	if (length/2) % 2 == 0:
	        		s = s
	        	else:
	        		s = s + step
	        	tag = 1
	        elif tag == 1:
	        	s = s + step
	        	tag = 2
        	length /= 2
        	step *= 2


        # while len(a) > 1:
        # 	a = a[1::2]
        # 	a = a[::-1]
        return s
for i in range(1, 50):
	print Solution().lastRemaining(i)