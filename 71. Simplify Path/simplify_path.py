#-*- coding: UTF-8 -*-

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        arr = [x for x in path.split('/') if x != '']
        stack = []
        for ele in arr:
            if ele == '.':
                continue
            if ele == '..':
                if(len(stack) > 0):
                    stack.pop()
            else:
                stack.append(ele)
        return '/'+'/'.join([ele for ele in stack])

if __name__ == '__main__':
    solu = Solution()
    path = "/../"
    res = solu.simplifyPath(path)
    print(res)