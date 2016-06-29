class Solution(object):
	def binary_search(self, tar, x):
		l = 0
		r = len(x)
		ret = 0
		while l <= r:
			mid = (l+r)/2
			# print l, r, mid, x[mid], tar, 'bina'
			if x[mid][0]<tar:
				l = mid+1
			else:
				ret = mid
				r = mid-1
		return ret 

	def get_ans(self, height):
		queue = [(height[0], 0)]
		ans = 0
		# print height
		for i in range(1, len(height)):
			if height[i] > queue[-1][0]:
				queue.append((height[i], i))
			else:
				farest_id = self.binary_search(height[i], queue)
				# print queue, height[i], farest_id
				farest_pos = queue[farest_id][1]
				# print height[i], i, farest_pos
				ans = max(ans, (i-farest_pos)*height[i])
		# print ans
		return ans

	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		return max(self.get_ans(height[::-1]), self.get_ans(height))

Solution().maxArea([423,4342,5324,1,34,432,423,523,3])