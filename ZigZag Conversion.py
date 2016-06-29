class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
        	return s
        res = []
        for i in range(numRows):
        	for k in range(len(s)):
        		fi = -i+(2*numRows-2)*k
        		se = i+(2*numRows-2)*k
        		if fi >= len(s):
        			break
        		if i not in [0, numRows-1] and fi>=0:
        			res.append(s[fi])
        		if se < len(s):
        			res.append(s[se])
        res = ''.join(res)
        print res
        return res