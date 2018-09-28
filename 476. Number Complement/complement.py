#-*- coding: UTF-8 -*-

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 求一个二进制数的补数
        binary = bin(num)[2:]
        string = ""
        for i in binary:
            if i=='0':
                string += '1'
            else:
                string += '0'
        res = int(string, 2)
        return res

    # 按位滑动
    def findComplement2(self, num):
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num

    # 和1...1求异或
    def findComplement3(self, num):
        return num ^ ((1 << num.bit_length()) - 1)

if __name__ == '__main__':
    solu = Solution()
    num = 7
    print(1<<num.bit_length())
    res = solu.findComplement2(num)
    print(res)
