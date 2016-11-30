class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2:
        	return 0
        ret = 0
        pos = 0 
        for i in range(2, len(A)):
        	if A[i]-A[i-1] != A[i-1]-A[i-2]:
        		n = i-pos
        		ret += sum([n-j+1 for j in range(3, n+1)])
        		pos = i-1
        n = len(A)-pos
        if n >= 3:
        	ret += sum([n-j+1 for j in range(3, n+1)])
        return ret 

print Solution().numberOfArithmeticSlices([1,1,2,5,6])