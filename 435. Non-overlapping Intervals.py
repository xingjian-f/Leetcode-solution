# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x.end)
        ret = 0
        if len(intervals) == 0:
        	return 0
        pos = intervals[0].end
        for i in intervals[1:]:
        	if i.start < pos:
        		ret += 1
        	else:
        		pos = i.end
        return ret 