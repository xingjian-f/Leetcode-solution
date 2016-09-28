class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        left = 0
        left_pos = -1
        num = 0
        for idx, i in enumerate(s):
        	if left == 0:
        		if i.isdigit():
        			num = num * 10 + int(i)
        		elif i == '[':
        			left += 1
        			left_pos = idx
        		else:
        			ret.append(i)
        	else:
        		if i == '[':
        			left += 1
        		elif i == ']':
        			left -= 1
        			if left == 0:
        				ret.append(num * self.decodeString(s[left_pos+1:idx]))
        				num = 0
        # print s, ret
        return ''.join(ret)

print Solution().decodeString('3[a]2[bc]')
print Solution().decodeString("3[a2[c]]")
print Solution().decodeString("2[abc]3[cd]ef")
print Solution().decodeString("ab1[a2[3[a]]]")