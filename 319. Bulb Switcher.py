class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in xrange(1, n+1):
        	if i*i <= n:
        		ret += 1
        	else:
        		break
        return ret

print Solution().bulbSwitch(10)