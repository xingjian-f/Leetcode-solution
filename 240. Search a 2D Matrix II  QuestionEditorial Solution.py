class Solution(object):
	def DQ(self, matrix, target, rows, rowe, cols, cole):
		print rows, rowe, cols, cole
		if rowe <= rows or cole <= cols:
			return False
		midn = (rows+rowe)/2
		midm = (cols+cole)/2
		if matrix[midn][midm] == target:
			return True
		elif matrix[midn][midm] < target:
			# return (self.searchMatrix(matrix[:midn+1,midm+1:], target) or 
			# 	self.searchMatrix(matrix[midn+1:,:midm+1], target) or
			# 	self.searchMatrix(matrix[midn+1:,midm+1:], target))
			return (self.DQ(matrix, target, rows, midn+1, midm+1, cole) or
				self.DQ(matrix, target, midn+1, rowe, cols, midm+1) or
				self.DQ(matrix, target, midn+1, rowe, midm+1, cole))
		else:
			# return (self.searchMatrix(matrix[:midn,:midm], target) or
			# 	self.searchMatrix(matrix[:midn,midm:], target) or 
			# 	self.searchMatrix(matrix[midn:,:midm], target))
			return (self.DQ(matrix, target, rows, midn, cols, midm) or
				self.DQ(matrix, target, rows, midn, midm, cole) or
				self.DQ(matrix, target, midn, rowe, cols, midm))


	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		return self.DQ(matrix, target, 0, len(matrix), 0, len(matrix[0]))