class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
        	return 0
        total = sum(A)
        tem_sum = 0
        for i in range(1, len(A)):
        	tem_sum += (i-1) * A[i]
        tem_sum += A[0]*(len(A)-1)
        ret = tem_sum
        for i in range(1, len(A)):
        	tem_sum = tem_sum - (total-A[i]) + A[i] * (len(A)-1)
        	ret = max(ret, tem_sum)
        return ret 

print Solution().maxRotateFunction([1,2,3])