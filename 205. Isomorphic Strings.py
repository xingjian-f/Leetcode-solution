class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        trans = {}
        vis = set()
        for i in range(len(s)):
        	if s[i] not in trans:
        		if t[i] in vis:
        			return False
        		trans[s[i]] = t[i]
        		vis.add(t[i])
        	else:
        		if trans[s[i]] != t[i]:
        			return False
        return True


print Solution().isIsomorphic("ab", "aa")