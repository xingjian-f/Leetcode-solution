class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for i in str(int(''.join(map(str, digits)))+1)]

Solution().plusOne([0])