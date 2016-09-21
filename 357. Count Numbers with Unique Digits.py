class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        nums2 = Counter(nums2)
        nums1 = Counter(nums1)
        ret = []
        for i in nums1:
        	cnt = min(nums1[i], nums2.get(i, 0))
        	for j in range(cnt):
        		ret.append(i)
        return ret

print Solution().intersect([1,2,3,2], [2,2])