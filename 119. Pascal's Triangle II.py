class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        ret = [1]
        for i in range(1, rowIndex):
        	ret.append(ret[-1]*(rowIndex-i)/i)
        return ret 

print Solution().getRow(100)