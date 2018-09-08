#-*- coding: UTF-8 -*-
import numpy

class Solution(object):
    # 数学方法
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        return int(n ** 0.5)

    # 根据逻辑来依次迭代
    def bulbSwitch2(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n + 1)
        a = numpy.array(a)
        for i in xrange(1, n + 1):
            a[::i] = 1 - a[::i]
        return sum(a[1:])

if __name__ == '__main__':
    solu = Solution()
    while(1):
        n = int(raw_input())
        res = solu.bulbSwitch2(n)
        print(res)