class Solution(object):
    def longestValidParentheses(self, s_in):
        """
        :type s: str
        :rtype: int
        """
        if len(s_in) <= 1:
            return 0
        s1 = []
        for i in s_in[::-1]:
            if i == ')':
                s1.append('(')
            else:
                s1.append(')')
        ans = 0
        for s in [s1, s_in]:
            posl = 0
            posr = 0
            cntl = 0
            cntr = 0
            if s[0] == '(':
                cntl += 1
            else:
                cntr += 1
            while posr < len(s):
                # print posl, posr
                cnt = cntl-cntr
                if cnt < 0:
                    if posl == posr:
                        posr += 1
                        posl += 1
                        cntl = 0
                        cntr = 0
                        if posr < len(s):
                            if s[posr] == '(':
                                cntl += 1
                            else:
                                cntr += 1
                    else:
                        if s[posl] == '(':
                            cntl -= 1
                        else:
                            cntr -= 1
                        posl += 1
                else:
                    if cnt == 0:
                        ans = max(ans, cntr + cntl)
                        # print posl, posr, ans
                    posr += 1
                    if posr < len(s):
                        if s[posr] == '(':
                            cntl += 1
                        else:
                            cntr += 1
        print ans
        return ans

Solution().longestValidParentheses(")))(((())()())))((()))))))))))))(((((((((((((((((((())))))))))))))))()()))))))(((((((())))))))))(()())())))(((((((()()()()()()()()())))))(((())()()()))((())))(((((((((())))))))))))))))))(((((((()))))))))))))))))()()()()()()()))))))))())))((((((()))))())))((((((()()()))))(((((((")