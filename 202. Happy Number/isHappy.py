#-*- coding: UTF-8 -*-

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1):
            return True
        seen = [n]
        while(n!=1):
            string = str(n)
            sum = 0
            for i in range(len(string)):
                sum += int(string[i])**2
            n = sum
            if n not in seen:
                seen.append(n)
            else:
                return False
        return True

if __name__ == '__main__':
    solu = Solution()
    n = 2
    res = solu.isHappy(n)
    print(res)
