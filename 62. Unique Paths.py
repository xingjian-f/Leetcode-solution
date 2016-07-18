class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n+m==2:
        	return 1
        if n==0 or m==0:
        	return 0
        ret = 1
        for i in range(m, m+n-1):
        	ret *= i
        for i in range(1, n):
        	ret /= i  
        return ret 