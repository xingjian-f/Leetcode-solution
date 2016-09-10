class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
        	return 1
        from heapq import heappop, heappush

        base = [(primes[i], 0, primes[i]) for i in range(len(primes))]
        ugly = [1]
        for i in range(n-1):
        	while True:
        		val, idx, p_base = heappop(base)
        		if val <= ugly[-1]:
        			heappush(base, (p_base*ugly[idx+1], idx+1, p_base))
        		else:
        			break
        	ugly.append(val)
        	heappush(base, (p_base*ugly[idx+1], idx+1, p_base))
        # print ugly
        return ugly[n-1]


print Solution().nthSuperUglyNumber(100000, [2, 7, 13, 19])