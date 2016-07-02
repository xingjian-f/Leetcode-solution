class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle in haystack:
        # 	return haystack.index(needle)
        # return -1
        pos = 0
        while pos+len(needle) <= len(haystack):
        	tag = True
        	max_part = 0
        	for i in range(len(needle)):
        		# print needle[i], haystack[pos+i]
        		if needle[i] == haystack[pos+i]:
        			if i>1 and needle[i] == needle[max_part]:
        				max_part += 1
        			else:
        				max_part = 0
        				if needle[i] == needle[max_part]:
        					max_part += 1
        		else:
        			pos += max(1, i-max_part)
        			tag = False
        			break
        	# print pos, tag
        	if tag:
        		return pos
        return -1

print Solution().strStr("mississippi","issip")
print Solution().strStr("mississippi", "issi")