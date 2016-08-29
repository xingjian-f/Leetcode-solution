class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0 or k == 0:
        	return False
        from collections import deque
        increase = deque([(nums[0], 0)])
        decrease = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
        	val = nums[i]
        	largest = nums[i-1]
        	smallest = nums[i-1]
        	while i-increase[-1][1] > k:
        		increase.pop()
        	largest = increase[-1][0]
        	while i-decrease[-1][1] > k:
        		decrease.pop()
        	smallest = decrease[-1][0]
        	if abs(val - largest) <= t or abs(val - smallest) <= t:
        		return True
        	while len(increase) > 0 and val >= increase[0]:
        		increase.popleft()
        	increase.appendleft((val, i))
        	while len(decrease) > 0 and val <= decrease[0]:
        		decrease.popleft()
        	decrease.appendleft((val, i))
        return False

print Solution().containsNearbyAlmostDuplicate([-1, -2, 4, 2, -4, 3, 4], 4, 0)