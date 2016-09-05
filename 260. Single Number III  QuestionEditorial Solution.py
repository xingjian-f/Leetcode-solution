class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		digits = [0 for i in range(100)]
		neg_digits = [0 for i in range(100)]
		for i in nums:
			tem = abs(i)
			cnt = 0
			while tem > 0:
				if i < 0:
					neg_digits[cnt] += tem % 2
				else:
					digits[cnt] += tem % 2
				tem /= 2
				cnt += 1 

		tag = 1
		tar = -1
		for i in range(len(digits)):
			if digits[i]%2 == 1:
				tar = i
				break
		if tar == -1:
			tag = -1
			for i in range(len(neg_digits)):
				if neg_digits[i]%2 == 1:
					tar = i 
					break
		# print digits
		# print tar        
		nums1 = 0
		nums2 = 0
		# tem1 = []
		# tem2 = []
		for i in nums:
			if tag*i >= 0 and i & 2**(tar) != 0:
				# print i, 2**(tar)
				# tem1.append(i)
				nums1 = nums1 ^ i
			else:
				# print i, 'a'
				# tem2.append(i)
				nums2 = nums2 ^ i
		# print sorted(tem1), len(tem1)
		# print sorted(tem2), len(tem2)
		return [nums1, nums2]

# print Solution().singleNumber([-1, 1, 2,2 ])