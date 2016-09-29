class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = num
        nbits = 32
        return hex((val + (1 << nbits)) % (1 << nbits))[2:]

print Solution().toHex(26)