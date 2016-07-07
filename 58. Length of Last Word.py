class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = map(len, s.split(' '))
        for i in reversed(s):
        	if i > 0:
        		return i 
        return 0