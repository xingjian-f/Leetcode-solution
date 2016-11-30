class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        ret = 0
        pos = 0
        for i in range(len(g)):
        	while pos<len(s) and s[pos] < g[i]:
        		pos += 1
        	if pos >= len(s):
        		break
        	ret += 1
        	pos += 1
        return ret 
