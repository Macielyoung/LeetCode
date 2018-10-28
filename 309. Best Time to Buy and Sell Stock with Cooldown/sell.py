#-*- coding: UTF-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        even, odd, oldEven = 0, float('-inf'), 0
        for price in prices:
            even, odd, oldEven = max(even, odd + price), max(odd, oldEven - price), even
        return even

if __name__ == '__main__':
    solu = Solution()
    prices = [1,2,3,0,2,1,4,7,9]
    res = solu.maxProfit(prices)
    print(res)