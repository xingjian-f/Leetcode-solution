class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        length = len(s)
        start = 0
        ans = 0
        for i in range(length):
        	cha = s[i]
        	if cha in record:
        		ans = max(ans, i-start)
        		cha_last_pos = record[cha]
        		for j in range(start, cha_last_pos+1):
        			del record[s[j]]
        		start = cha_last_pos+1
        	record[cha] = i
        ans = max(ans, length-start)
       	return ans 

a = Solution()
test_case = [
	'a',
	'',
	'aaa',
	'abacd',
	'dvdf',
	"abcabcbb"
]
for i in test_case:
	print a.lengthOfLongestSubstring(i)