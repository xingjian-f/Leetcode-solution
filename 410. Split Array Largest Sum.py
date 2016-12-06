class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def split(nums, large):
        	ret = 1
        	total = 0
        	for i in nums:
        		if i > large:
        			return 1e9
        		if total + i > large:
        			ret += 1
        			total = i 
        		else:
        			total += i 
        	return ret 

        l = 0
        r = sum(nums)+1
        ret = r-1
        while l < r:
        	mid = (l+r) / 2
        	nb = split(nums, mid)
        	# print mid, nb
        	if nb <= m:
        		ret = mid
        		r = mid
        	else:
        		l = mid+1
        return ret

print Solution().splitArray([1,3],2)