#-*- coding: UTF-8 -*-

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        for i in range(len(prices)-1):
            max_profit = max(max(prices[i+1:])-prices[i], max_profit)
        if(max_profit < 0):
            return 0
        else:
            return max_profit

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

if __name__ == '__main__':
    solu = Solution()
    prices = [7,1,5,3,6,4]
    max_profit = solu.maxProfit2(prices)
    print(max_profit)