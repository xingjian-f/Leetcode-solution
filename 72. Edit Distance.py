class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
        	return len(word2)
        if len(word2) == 0:
        	return len(word1)
        dp = [[1e9 for j in range(len(word2))] for i in range(len(word1))]
        tag = False
        for i in range(len(word1)):
        	if word2[0] == word1[i]:
        		tag = True
        	if tag:
        		dp[i][0] = i
        	else:
        		dp[i][0] = i+1
        tag = False 
        for i in range(len(word2)):
        	if word1[0] == word2[i]:
        		tag = True
        	if tag == False:
        		dp[0][i] = i+1
        	else:
        		dp[0][i] = i
      	for i in range(1, len(word1)):
      		for j in range(1, len(word2)):
      			if word1[i] == word2[j]:
      				dp[i][j] = dp[i-1][j-1]
      			else:
      				dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
      	return dp[len(word1)-1][len(word2)-1]

print Solution().minDistance("a",
"ab")