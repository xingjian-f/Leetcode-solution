class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        posl = 0
        posr = len(nums)
        ans = len(nums)
        while posl < posr:
        	mid = (posl+posr) / 2
        	if nums[mid] == target:
        		ans = mid
        		break
        	elif nums[mid] < target:
        		posl = mid+1
        	else:
        		ans = mid
        		posr = mid
        return ans 