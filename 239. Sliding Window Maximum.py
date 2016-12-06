class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if len(nums) == 0:
        	return []
        ret = []
        queue = deque([])
        for i in range(len(nums)):
        	while len(queue) > 0 and nums[i]>=queue[-1][0]:
        		queue.pop()
        	queue.append((nums[i],i))
        	if i >= k-1:
        		while i-queue[0][1] >= k:
        			queue.popleft()
        		ret.append(queue[0][0])
        	# print queue
        return ret 

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 8)