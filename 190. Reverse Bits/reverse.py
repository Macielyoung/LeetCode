#-*- coding: UTF-8 -*-

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nums = []
        while(n > 0):
            c = n & 1
            nums.append(c)
            n = n >> 1
        while(len(nums) < 32):
            nums.append(0)
        string = "".join(str(i) for i in nums)
        n1 = int(string, 2)
        return n1

    def reverseBits2(self, n):
        r = 0
        for i in range(32):
            # 右移一位，每次最低位都是0，下面要使用或运算来保存当前位的数字
            r <<= 1
            r |= n & 1
            n >>= 1
        return r

if __name__ == '__main__':
    solu = Solution()
    n = 43261596
    res = solu.reverseBits2(n)
    print(res)