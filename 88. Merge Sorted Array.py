class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            del nums1[m]
        for i in range(n, len(nums2)):
            del nums2[n]
        print nums1, nums2
        nums1.extend(nums2)
        nums1.sort()