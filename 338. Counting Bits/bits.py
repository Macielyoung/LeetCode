#-*- coding: UTF-8 -*-

class Solution:
    # 时间复杂度O(n*sizeof(integer))
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            n = 0
            while(i>0):
                if(i & 1):
                    n += 1
                i >>= 1
            res.append(n)
        return res

    # 时间复杂度O(n)
    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) < num + 1:
            res += [i + 1 for i in res]
        return res[:num + 1]


if __name__ == '__main__':
    solu = Solution()
    num = 8
    res = solu.countBits2(num)
    print(res)