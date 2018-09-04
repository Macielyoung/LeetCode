#-*- coding: UTF-8 -*-

class Solution:
    # 超时
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglys = [1]
        ugly2 = ugly3 = ugly5 = 0
        while(len(uglys)<n):
            ugnext2, ugnext3, ugnext5 = uglys[ugly2]*2, uglys[ugly3]*3, uglys[ugly5]*5
            if (ugnext2 <= ugnext3 and ugnext2 <= ugnext5):
                ugly2 += 1
                if(ugnext2 not in uglys):
                    uglys.append(ugnext2)
                continue
            if (ugnext3 <= ugnext2 and ugnext3 <= ugnext5):
                ugly3 += 1
                if(ugnext3 not in uglys):
                    uglys.append(ugnext3)
                continue
            if (ugnext5 <= ugnext2 and ugnext5 <= ugnext3):
                ugly5 += 1
                if(ugnext5 not in uglys):
                    uglys.append(ugnext5)
                continue
        return uglys

    def nthUglyNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

if __name__ == '__main__':
    solu = Solution()
    n = 10
    res = solu.nthUglyNumber2(n)
    print(res)