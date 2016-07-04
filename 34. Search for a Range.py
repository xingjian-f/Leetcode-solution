class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ansl = -1
        ansr = -1
        posl = 0
        posr = len(nums)
        while posl < posr:
        	mid = (posl+posr)/2
        	if nums[mid] == target:
        		ansl = mid
        		posr = mid
        	elif nums[mid] < target:
        		posl = mid+1
        	else:
        		posr = mid
        posl = 0
        posr = len(nums)
        while posl < posr:
        	mid = (posl + posr) /2
        	if nums[mid] == target:
        		ansr = mid
        		posl = mid+1
        	elif nums[mid] < target:
        		posl = mid+1
        	else:
        		posr = mid
        return [ansl, ansr]