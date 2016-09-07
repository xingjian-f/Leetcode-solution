class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        cnt = [0 for i in range(len(citations)+1)]
        for i in citations:
        	i = min(i, len(citations))
        	cnt[i] += 1

       	tem = 0
       	ret = 0
       	for i in range(len(citations)+1):
       		if len(citations) - tem >= i:
       			ret = i
       		tem += cnt[i]
       	return ret 


print Solution().hIndex([0,3,1,4, 4, 2, 5, 6])