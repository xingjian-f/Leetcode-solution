class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        expr = '+-*/'
        for i in tokens:
        	if i in expr:
        		# print s
        		num1 = s[-2]
        		num2 = s[-1]
        		s.pop()
        		s.pop()
        		if i == '+':
        			s.append(num1 + num2)
        		elif i == '-':
        			s.append(num1 - num2)
        		elif i == '*':
        			s.append(num1 * num2)
        		else:
        			# print num1, num2, num1/num2
        			if num1*num2 < 0:
        				s.append(- (abs(num1) / abs(num2)))
        			else:
        				s.append(num1 / num2)
        	else:
        		s.append(int(i))
        return s[0]

print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print -(1/2)