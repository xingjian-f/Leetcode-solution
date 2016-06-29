class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
        	x = '-' + x[1:][::-1]
        else:
        	x = x[::-1]
        x = int(x)
        if x > 2147483647 or x < -2147483648:
        	x = 0
        return int(x)


print Solution().reverse(1231237129846213949712387414120398412)