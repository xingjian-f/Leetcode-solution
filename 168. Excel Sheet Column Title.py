class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n > 0:
        	if n % 26 == 0:
        		ret.append('Z')
        		n = n/26 - 1
        	else:
        		ret.append(chr(ord('A')+n%26-1))
        		n = n / 26
        return ''.join(ret[::-1])

print Solution().convertToTitle(26*28)