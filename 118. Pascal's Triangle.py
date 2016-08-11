class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
        	ret.append([1])
        	if i > 0:
        		for j in range(1,i):
        			ret[-1].append(ret[-2][j-1]+ret[-2][j])
        		ret[-1].append(1)
        return ret 


print Solution().generate(0)