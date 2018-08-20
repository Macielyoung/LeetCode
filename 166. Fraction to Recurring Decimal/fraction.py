#-*- coding: UTF-8 -*-

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        res = ""
        seen = {}
        neg = (numerator<0) ^ (denominator<0)
        if neg:
            res += '-'
        divided_res = int(abs(numerator) / abs(denominator))
        res += str(divided_res)
        remainder = abs(numerator) % abs(denominator)
        # 整数
        if remainder == 0:
            return res
        else:
            res += '.'
        i = 0
        while remainder != 0 and remainder not in seen:
            seen[remainder] = i
            remainder *= 10
            res += str(int(remainder / abs(denominator)))
            remainder = remainder % abs(denominator)
            i += 1
        # 有限小数
        if remainder == 0:
            return res
        # 无限循环小数
        else:
            index = seen[remainder]
            dot_position = res.index('.')
            return res[: dot_position + 1 + index] + '(' + res[dot_position + 1 + index:] + ')'

if __name__ == '__main__':
    solu = Solution()
    numerator = 7
    denominator = -12
    res = solu.fractionToDecimal(numerator, denominator)
    print(res, type(res))