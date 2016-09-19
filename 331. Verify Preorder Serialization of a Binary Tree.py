class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '#':
        	return True
        preorder = preorder.split(',')
        stack = []
        for idx,i in enumerate(preorder):
        	# print stack, i
        	if i == '#':
        		if len(stack) == 0:
        			return False
        		stack.pop()
        		if len(stack) == 0 and idx != len(preorder)-1:
        			return False
        	else:
        		if len(stack) > 0:
        			stack.pop()
        		stack.append(i)
        		stack.append(i)
        # print stack
        return len(stack) == 0

print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print Solution().isValidSerialization("#")
print Solution().isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#")