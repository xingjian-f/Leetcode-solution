class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        cnt = 0
        last = 1
        for i in range(1, num+1):
        	cnt += 1
        	ret.append(1 + ret[i-last])
        	if cnt == last:
        		last = last*2
        		cnt = 0
        return ret

for i in range(50):
	
	print i, sum(map(int,bin(i)[2:])), Solution().countBits(i)