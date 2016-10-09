class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(s)
        ret = 0
        for i in cnt.values():
        	if i > 0:
        		if i%2 == 0:
        			ret += i 
        		else:
        			if i > 1:
        				ret += i-1
        			if ret%2==0:
        				ret += 1
        return ret 

print Solution().longestPalindrome('aaa')