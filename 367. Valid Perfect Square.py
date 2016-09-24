class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = int(1e5)
        while l < r:
        	mid = (l + r) / 2
        	tem = mid * mid
        	if tem == num:
        		return True
        	elif tem > num:
        		r = mid
        	else:
        		l = mid+1
        return False

print Solution().isPerfectSquare(16) 