class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        ret = []
        i = 0
        while i < len(num):
        	min_digit = num[i]
        	pos = i
        	for j in range(1, k+1):
        		if i+j < len(num) and num[i+j] < min_digit:
        			min_digit = num[i+j]
        			pos = i+j
        	ret.append(min_digit)
        	k -= pos-i
        	i = pos + 1
        # print ret, k
        if k >= 1:
        	ret = ret[:-k]
        # print ret
        if len(ret) == 0:
        	return '0'
        return str(int(''.join(ret)))

print Solution().removeKdigits('042434', 1)