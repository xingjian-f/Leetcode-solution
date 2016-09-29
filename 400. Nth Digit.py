class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_len = 1
        while True:
        	digit_total = 9 * 10 ** (digit_len-1) * digit_len
        	if n > digit_total:
        		n -= digit_total
        		digit_len += 1
        	else:
        		idx = 10 ** (digit_len-1) + n / digit_len - 1
        		str_idx = n % digit_len
        		if str_idx == 0:
        			return int(str(idx)[-1])
        		else:
        			return int(str(idx+1)[str_idx-1])

# for i in range(900,1050):
# 	print Solution().findNthDigit(i)