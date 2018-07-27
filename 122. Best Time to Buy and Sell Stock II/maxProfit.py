#-*- coding: UTF-8 -*-

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        num = len(prices)
        for i in range(num-1):
            if(prices[i+1]>prices[i]):
                maxProfit += prices[i+1]-prices[i]
        return maxProfit


if __name__ == '__main__':
    solu = Solution()
    prices = [7,1,5,3,6,4]
    res = solu.maxProfit(prices)
    print(res)
