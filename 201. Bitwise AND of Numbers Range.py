class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == 0:
        	return 0
        k = 0
        tem = 1
        while True:
        	if tem * 2 <= n:
        		k += 1
        		tem *= 2
        	else:
        		break
        if m < tem:
        	return 0
        else:
        	return 2**k + self.rangeBitwiseAnd(m-tem, n-tem)

# print Solution().rangeBitwiseAnd(1, 3)
for i in range(100):
	for j in range(i,100):
		if Solution().rangeBitwiseAnd(i, j) != 0:
			print i, j, Solution().rangeBitwiseAnd(i, j)