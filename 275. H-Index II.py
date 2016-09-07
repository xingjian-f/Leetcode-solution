class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        posl = 0
        posr = len(citations)
        ret = 0
        while posl < posr:
        	mid = (posl + posr) / 2
        	num = len(citations)-mid
        	if citations[mid] >= num:
        		ret = num
        		posr = mid
        	else:
        		posl = mid+1
        return ret

print Solution().hIndex([0,1])