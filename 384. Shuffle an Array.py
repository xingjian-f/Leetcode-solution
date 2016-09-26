class Solution(object):
    
    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        # from random import shuffle
        # self.iter = shuffle(nums)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        # from random import shuffle
        # self.iter = shuffle(self.nums)
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from copy import deepcopy
        from random import shuffle
        a = deepcopy(self.nums)
        shuffle(a)
        return a


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2])
print obj.reset()
print obj.shuffle()