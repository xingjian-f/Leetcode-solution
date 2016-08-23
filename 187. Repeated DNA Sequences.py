class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        record = {}
        for i in range(len(s)-9):
        	record[s[i:i+10]] = record.get(s[i:i+10], 0) + 1
        ret = []
        for i in record:
        	if record[i] > 1:
        		ret.append(i)
        return ret 

print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")