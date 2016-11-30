# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def bisearch(self, x, a):
		l = 0
		r = len(a)
		ret = -1
		while l < r:
			mid = (l + r) / 2
			val = a[mid][1][0]
			if val >= x:
				ret = a[mid][0]
				r = mid
			else:
				l = mid+1
		return ret


	def findRightInterval(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[int]
		"""
		intervals = [[i.start, i.end] for i in intervals]
		tem = [i for i in enumerate(intervals)]
		tem = sorted(tem, key=lambda x:x[1][0])
		ret = [self.bisearch(i[1], tem) for i in intervals]
		return ret


print Solution().findRightInterval( [ [1,4], [2,3], [3,4] ]) 