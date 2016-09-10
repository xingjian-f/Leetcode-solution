class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = [0]
        for i in nums:
            self.dp.append(self.dp[-1] + i)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1]-self.dp[i]


# Your NumArray object will be instantiated and called as such:
numArray = NumArray( [-2, 0, 3, -5, 2, -1])
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)