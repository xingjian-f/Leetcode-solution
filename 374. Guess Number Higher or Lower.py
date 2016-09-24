# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n+1
        while l < r:
        	mid = (l + r) / 2
        	res = guess(mid)
        	if res == -1:
        		r = mid
        	elif res == 1:
        		l = mid
        	else:
        		return mid