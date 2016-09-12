class Node(object):
    def __init__(self, val, left_node, right_node, left_range, right_range):
        self.val = val
        self.left_node = left_node
        self.right_node = right_node
        self.left_range = left_range
        self.right_range = right_range


class NumArray(object):
    def build(self, left_range, right_range):
        # print left_range, right_range
        if left_range == right_range:
            val = self.nums[left_range]
            node = Node(val, None, None, left_range, right_range)
        else:
            mid = (left_range + right_range) / 2
            left_node, left_val = self.build(left_range, mid)
            right_node, right_val = self.build(mid+1, right_range)
            val = left_val + right_val 
            node = Node(val, left_node, right_node, left_range, right_range)

        return (node, val)


    def modify(self, node, i, to_val):
        left_range = node.left_range
        right_range = node.right_range
        left_node = node.left_node
        right_node = node.right_node
        ori_val = node.val 

        if left_range == right_range:
            node.val = to_val
            return to_val - ori_val
        else:
            mid = (left_range + right_range) / 2
            if i <= mid:
                next_node = left_node
            else:
                next_node = right_node

            node.val += self.modify(next_node, i, to_val)
            return node.val - ori_val


    def query(self, q_left, q_right, node):
        left_range = node.left_range
        right_range = node.right_range
        left_node = node.left_node
        right_node = node.right_node
        ori_val = node.val 

        if q_left == left_range and q_right == right_range:
            return ori_val

        mid = (left_range + right_range) / 2
        ret = 0
        if q_left <= mid:
            ret += self.query(q_left, min(mid, q_right), left_node)
        if q_right > mid:
            ret += self.query(max(q_left, mid+1), q_right, right_node)
        return ret       


    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        if len(nums) == 0:
            return
        self.root = self.build(0, len(nums)-1)[0]


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.modify(self.root, i, val)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(i, j, self.root)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray([])
# print numArray.sumRange(0, 0)
# print numArray.update(1, 10)
# print numArray.sumRange(0, 1)