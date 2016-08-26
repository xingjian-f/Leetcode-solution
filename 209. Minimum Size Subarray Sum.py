class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        pos1 = 0
        pos2 = 0
        tem = nums[0]
        ret = 1e9
        while True:
        	if tem >= s:
        		# print pos2, pos1, tem
        		ret = min(ret, pos2+1-pos1)
        		tem -= nums[pos1]
        		pos1 += 1
        		pos2 = max(pos1, pos2)
        	else:
        		pos2 += 1
        		if pos2 >= len(nums):
        			break
        		tem += nums[pos2]

        if ret == 1e9:
        	return 0
        return ret

print Solution().minSubArrayLen(7, [1, 2, 3])