class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		if len(s)>12:
			return []
		from itertools import combinations
		res = []
		for i in combinations(range(len(s)-1), 3):
			tag = True
			test = [(0, i[0]+1), (i[0]+1, i[1]+1), (i[1]+1, i[2]+1), (i[2]+1, len(s))]
			for j in test:
				tag = tag and int(s[j[0]:j[1]]) <= 255 and not (j[1]>j[0]+1 and s[j[0]] == '0')
			if tag:
				tmp = []
				for j in range(len(s)):
					tmp.append(s[j])
					if j in i:
						tmp.append('.')
				res.append(''.join(tmp))
		return res

print Solution().restoreIpAddresses('055255111')