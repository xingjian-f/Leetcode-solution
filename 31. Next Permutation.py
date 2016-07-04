class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        max_num = -1e9
        tag = False
        for i in range(1, len(nums)+1):
        	if nums[-i] < max_num:
        		tag= True
        		pos = None
        		min_gre = 1e9
        		for j in range(1, i):
        			if nums[-j]>nums[-i] and nums[-j]<min_gre:
        				min_gre = nums[-j]
        				pos = j
        		
        		rem = []
        		for j in range(1, i+1):
        			if j != pos:
        				# print j, pos, nums[-j]
        				rem.append(nums[-j])
        		# print rem, pos, i
        		nums[-i] = nums[-pos]
        		nums[-i+1:] = sorted(rem)

        		break
        	else:
        		max_num = max(max_num, nums[-i])
        if tag == False and len(nums)>0:
        	for i in range(len(nums)/2):
        		nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]

print Solution().nextPermutation([0, -1, -3])