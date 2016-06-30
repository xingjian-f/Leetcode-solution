class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		ret = []
		if len(strs)>0:
			for i in range(min(map(len,strs))):
				tag = True
				if len(strs) > 1:
					for j in range(1, len(strs)):
						tag = tag and strs[j][i] == strs[j-1][i]
				if tag:
					ret.append(strs[0][i])
				else:
					break
		ret = ''.join(ret)
		print ret 
		return ret

Solution().longestCommonPrefix([])