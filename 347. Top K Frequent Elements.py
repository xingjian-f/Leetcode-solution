class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
        	return nums
        cnt = {}
        for i in nums:
        	cnt[i] = cnt.get(i, 0) + 1
        ret = []
        import heapq
        for i in cnt:
        	heapq.heappush(ret, (cnt[i], i))
        	if len(ret) > k:
        		heapq.heappop(ret)
        return [i[1] for i in ret]


print Solution().topKFrequent([1],1)