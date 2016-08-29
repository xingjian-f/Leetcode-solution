class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cnt = {}
        for i in range(len(nums)):
        	if nums[i] not in cnt:
        		cnt[nums[i]] = [i]
        	else:
        		cnt[nums[i]].append(i)
        for i in cnt:
        	for j in range(1, len(cnt[i])):
        		if cnt[i][j]-cnt[i][j-1] <= k:
        			return True
        return False

print Solution().containsNearbyDuplicate([1,0,1,1],0)