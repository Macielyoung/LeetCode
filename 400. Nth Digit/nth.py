#-*- coding: UTF-8 -*-

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=9:
            return n

        def cal_total_digits(num):
            total_digits = 0
            i = 1
            while (i <= num):
                total_digits += (num - i + 1)
                i *= 10
            return total_digits

        j = 1
        # log(n) time for the while loop
        while (cal_total_digits(10 ** j - 1) <= n):
            curr_count = cal_total_digits(10 ** j - 1)
            j += 1

        remain = n - curr_count
        target = remain // j + 10 ** (j - 1) - 1
        mod = remain % j
        return int(str(target + 1)[mod - 1]) if mod else int(str(target)[-1])

if __name__ == '__main__':
    solu = Solution()
    n = 11
    res = solu.findNthDigit(n)
    print(res)