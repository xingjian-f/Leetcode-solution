class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = [0 for i in range(32)]
        tag = 0
        for i in nums:
        	if i < 0:
        		tag += 1
        	a = bin(abs(i))[2:][::-1]
        	for j in range(len(a)):
        		if a[j] == '1':
        			cnt[j] += 1
        s = []
        for i in cnt:
        	s.append(str(i%3))
        s = ''.join(s[::-1])
        ret = int(s, 2)
        if tag % 3 == 1:
        	ret = -ret
        return ret

print Solution().singleNumber([-1,-2,-2,-2,-1,-1,-3])