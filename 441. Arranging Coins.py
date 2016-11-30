class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n+1
        ret = None
        while l < r:
        	mid = (l + r) / 2
        	# print mid
        	if (1+mid) * mid / 2 <= n:
        		ret = mid
        		l = mid+1
        	else:
        		r = mid
        return ret

print Solution().arrangeCoins(1)