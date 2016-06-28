class Solution(object):		
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        nums = []
        pos1 = 0
        pos2 = 0
        while pos1 < len1 and pos2 < len2:
        	if nums1[pos1] < nums2[pos2]:
        		nums.append(nums1[pos1])
        		pos1 += 1
        	else:
        		nums.append(nums2[pos2])
        		pos2 += 1
        for i in range(pos1, len1):
        	nums.append(nums1[i])
        for i in range(pos2, len2):
        	nums.append(nums2[i])
        print nums
        if total%2==0:
        	return (nums[total/2-1]+nums[total/2])/2.0
        else:
        	return nums[total/2]

a = Solution()
print a.findMedianSortedArrays([1,3,3,5],[2,4])