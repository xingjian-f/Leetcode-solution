# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#     def __repr__(self):
#         return str(self.start) + ' ' + str(self.end)


class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inters = []


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        tag = 0
        for idx, i in enumerate(self.inters):
            s = i.start
            e = i.end
            if val <= e+1:
                tag = 1
            if val < s:
                if val == s-1:
                    if idx == 0 or self.inters[idx-1].end+1 != val:
                        self.inters[idx].start -= 1
                else:
                    self.inters.insert(idx, Interval(val, val))
                break
            elif val == e+1:
                if idx == len(self.inters)-1 or self.inters[idx+1].start-1 != val:
                    self.inters[idx].end += 1
                else:
                    self.inters[idx].end = self.inters[idx+1].end
                    del self.inters[idx+1]
                break

        if tag == 0:
            self.inters.append(Interval(val, val))


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        # print self.inters
        return self.inters


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(3)
obj.addNum(5)
obj.addNum(4)
obj.addNum(3)
obj.addNum(1)
obj.addNum(2)
obj.addNum(9)
obj.addNum(10)
obj.addNum(12)
obj.addNum(11)
print (obj.getIntervals())