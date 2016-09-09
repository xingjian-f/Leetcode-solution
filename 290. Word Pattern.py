class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = s.split()
        if len(pattern) != len(s) or len(s) == 0:
        	return False
        rec1 = {}
        rec2 = {}
        for i in range(len(s)):
        	if pattern[i] not in rec1 and s[i] not in rec2:
        		rec1[pattern[i]] = s[i]
        		rec2[s[i]] = pattern[i]
        	else:
        		if (pattern[i] not in rec1 or rec1[pattern[i]] != s[i] 
        			or s[i] not in rec2 or  rec2[s[i]] != pattern[i]):
        			return False

        return True

print Solution().wordPattern('a', 'dog')