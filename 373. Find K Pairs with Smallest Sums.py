class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        front = []
        if len(nums1) == 0 or len(nums2) == 0:
        	return []
        for i in range(len(nums1)):
        	heapq.heappush(front, (nums1[i]+nums2[0], i, 0))
        ret = []
        for _ in range(k):
        	if len(front) == 0:
        		return ret
        	top = heapq.heappop(front)
        	ret.append([nums1[top[1]], nums2[top[2]]])
        	if top[2]+1 < len(nums2):
        		heapq.heappush(front, (nums1[top[1]]+nums2[top[2]+1], top[1], top[2]+1))
        return ret 

print Solution().kSmallestPairs([1,1,2], [1,2,3], 10)