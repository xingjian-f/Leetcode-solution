class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        for i in ct:
        	if i not in cs or ct[i] > cs[i]:
        		return i