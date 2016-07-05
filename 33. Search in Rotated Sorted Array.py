class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
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

       	ans = -1
       	# print max_pos
        if target >= nums[0]:
        	posl = 0
        	posr = max_pos+1
        	while posl < posr:
        		mid = (posl+posr)/2
        		if nums[mid] < target:
        			posl = mid+1
        		elif nums[mid] == target:
        			ans = mid
        			break
        		else:
        			posr = mid
        else:
        	posl = max_pos+1
        	posr = len(nums)
        	while posl < posr:
        		mid = (posl+posr) / 2
        		if nums[mid] < target:
        			posl = mid+1
        		elif nums[mid] == target:
        			ans = mid
        			break
        		else:
        			posr = mid

        print ans
        return ans

Solution().search([1, 3], 1)