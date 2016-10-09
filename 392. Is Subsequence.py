class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        poss = 0
        post = 0
        while poss < len(s) and post < len(t):
        	if s[poss] == t[post]:
        		poss += 1
        	post += 1
        if poss == len(s):
        	return True
        return False

print Solution().isSubsequence('', '')