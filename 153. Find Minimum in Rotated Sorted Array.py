class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pos = len(nums) - 1
        posl = 0
        posr = len(nums)
        while posl < posr:
        	mid = (posl + posr) / 2
        	if nums[mid] <= nums[-1]:
        		posr = mid
        	else:
        		max_pos = mid
        		posl = mid+1

       	if max_pos == len(nums) - 1:
       		min_pos = 0
       	else:
       		min_pos = max_pos + 1
       	return nums[min_pos]


print Solution().findMin([3, 1, 2])