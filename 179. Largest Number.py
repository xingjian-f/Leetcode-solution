class Solution:
    # @param {integer[]} nums
    # @return {string}
    def compare(self, x, y):
    	# print x, y
    	for i in range(min(len(x), len(y))):
    		if x[i] < y[i]:
    			return -1
    		elif x[i] > y[i]:
    			return 1
    	if len(x) == len(y):
    		return 0
    	elif len(x) < len(y):
    		return self.compare(x, y[len(x):])
    	else:
    		return self.compare(x[len(y):], y)


    def largestNumber(self, nums):
    	nums = map(str, nums)
        nums = sorted(nums, cmp=lambda x, y: self.compare(x, y), reverse=True)
        s = len(nums)-1
        for i in range(len(nums)-1):
        	if nums[i] != '0':
        		s = i 
        		break
        # print nums[s:]
        return ''.join(nums[s:])

print Solution().largestNumber([3, 30, 34, 5, 9, 50, 12, 43, 90, 99])
# print Solution().compare('128', '12')
print Solution().largestNumber([0, 0, 1])