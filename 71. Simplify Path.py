class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathList = path.split("/")
        stack = []
        
        for elem in pathList:
            if elem == '..' and len(stack) != 0:
                stack.pop()
            elif elem != '.' and elem != '' and elem != '..':
                stack.append(elem)
                
        return '/' + '/'.join(stack)