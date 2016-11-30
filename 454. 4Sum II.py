class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        rec = defaultdict(int)
        for i in C:
        	for j in D:
        		total = i+j
        		rec[total] += 1
        ret = 0
        for i in A:
        	for j in B:
        		total = i+j
        		ret += rec[-total]
        return ret