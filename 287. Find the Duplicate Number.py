class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        posl = 1
        posr = len(nums)
        total = len(nums)-1
        ret = None
        while posl < posr:
        	mid = (posl + posr) / 2
        	cnt = 0
        	for i in nums:
        		if i >= mid:	
        			cnt += 1
        	if cnt > total-mid+1:
        		posl = mid+1 
        		ret = mid
        	else:
        		posr = mid
        return ret 

print Solution().findDuplicate([1,2,3,1,1,1])