# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        posl = 1
        posr = n+1
        ans = 0
        while posl < posr:
        	mid = (posl + posr) / 2
        	if isBadVersion(mid):
        		ans = mid
        		posr = mid
        	else:
        		posl = mid+1
        return ans