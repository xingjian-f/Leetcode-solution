class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i in s:
        	ret *= 26
        	ret += ord(i)-ord('A')+1
        	
        return ret