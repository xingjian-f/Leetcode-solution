class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) == 0:
        	return True
        if len(wordDict) == 0:
        	return False
        dp = range(len(s))
        if s[0] in wordDict:
        	dp[0] = True
        else:
        	dp[0] = False
        for i in range(1, len(s)):
        	dp[i] = False
        	for word in wordDict:
        		if len(word) <= i+1 and word == s[i-len(word)+1:i+1]:
        			if i+1 == len(word) or dp[i-len(word)]:
        				dp[i] = True
        				break 
        return dp[-1]