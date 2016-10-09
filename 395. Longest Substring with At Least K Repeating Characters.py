class Solution(object):
	def search(self, tar, pos):
		posl = 0
		posr = len(pos)
		ret = -1
		while posl < posr:
			mid = (posl + posr) / 2
			if pos[mid] <= tar:
				ret = pos[mid]
				posl = mid+1
			else:
				posr = mid
		return ret 


	def longestSubstring(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""
		cnt = [{} for i in range(len(s)+1)]
		for i in range(len(s)):
			for j in cnt[i]:
				cnt[i+1][j] = cnt[i][j]
			cnt[i+1][s[i]] = cnt[i+1].get(s[i], 0) + 1
		from collections import defaultdict
		pos = defaultdict(list)
		for i in range(len(s)):
			pos[s[i]].append(i)

		# print cnt
		ret = 0 
		for i in range(len(s)):
			left = -1
			while left < i:
				# print left, i 
				tag = 1
				for j in cnt[i+1]:
					nb = cnt[i+1][j]-cnt[left+1].get(j, 0)
					if nb > 0 and nb < k:
						# print j, nb
						left = max(left, self.search(i, pos[j]))
						tag = 0

				if tag == 1:
					break
			# print i, left
			ret = max(ret, i-left)
		return ret

print Solution().longestSubstring("bbaaacbc", 2)