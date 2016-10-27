class Node(object):
	def __init__(self, l, r, lson, rson):
		self.val = 0
		self.l = l 
		self.r = r
		self.lson = lson
		self.rson = rson 


class SegmentTree(object):
	def __init__(self, n):
		self.root = self.build(0, n) 


	def build(self, l, r):
		if l == r:
			return Node(l, r, None, None)
		mid = (l+r) / 2
		return Node(l, r, self.build(l, mid), self.build(mid+1, r))


	def modify(self, node, x):
		l = node.l 
		r = node.r
		if l == r:
			node.val += 1
			return node.val 
		mid = (l+r) / 2
		lson = node.lson
		rson = node.rson
		if x <= mid:
			node.val = self.modify(lson, x) + rson.val
		else:
			node.val = self.modify(rson, x) + lson.val
		return node.val


	def query(self, node, x, y):
		l = node.l
		r = node.r
		val = node.val
		lson = node.lson
		rson = node.rson
		mid = (l+r) / 2
		if x == l and y == r:
			return val
		ret = 0 
		if x <= mid: 
			ret += self.query(lson, x, min(y, mid))
		if y > mid:
			ret += self.query(rson, max(x, mid+1), y)
		return ret 


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
        	return []
        order = sorted(nums)
        idx = dict((i, idx) for idx, i in enumerate(order))
        for i in range(len(nums)):
        	nums[i] = idx[nums[i]]
        # print nums
        seg = SegmentTree(max(nums))
        ret = []
        for i in nums[::-1]:
        	seg.modify(seg.root, i)
        	if i == 0:
        		ret.append(0)
        	else:
        		ret.append(seg.query(seg.root, 0, i-1))
        return ret[::-1]


print Solution().countSmaller([2,2,2,2])