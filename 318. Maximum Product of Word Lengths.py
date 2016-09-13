class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        for i in range(len(words)):
        	words[i] = (set(words[i]), len(words[i]))

        # print words
        ret = 0
        for i in range(len(words)):
        	for j in range(i+1, len(words)):
        		tag = True
        		for k in words[i][0]:
        			if k in words[j][0]:
        				tag = False
        				break
        		if tag:
        			ret = max(ret, words[i][1]*words[j][1])

        return ret

print Solution().maxProduct(['a', 'b'])