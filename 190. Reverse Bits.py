class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(32):
        	ret += (n%2) * 2**(31-i)
        	n /= 2
        return ret