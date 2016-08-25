class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
        	return 0
        is_prime = [1 for i in xrange(n)]
        is_prime[1] = 0
        is_prime[0] = 0
        for i in xrange(2, n):
        	if is_prime[i] == 1:
        		for j in xrange(i*2, n, i):
        			is_prime[j] = 0
        # print is_prime
        return sum(is_prime)

print Solution().countPrimes(100)