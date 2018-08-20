#-*- coding: UTF-8 -*-
import sys

class Solution:
    # Time Limit Exceeded
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    # if(dp[i-coin] != sys.maxsize):
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return dp[-1] if dp[-1] < amount+1 else -1

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1

    # BFS
    def coinChange3(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        queue = []
        seen = set()
        for coin in coins:
            if amount == coin:
                return 1
            if amount > coin:
                queue.append((1, amount - coin))
                seen.add(amount - coin)

        if coins[-1] > amount:
            return -1

        coins_set = set(coins)
        while queue:
            entry = queue.pop(0)
            if entry[1] in coins_set:
                return entry[0] + 1

            for coin in coins:
                if coin < entry[1] and entry[1] - coin not in seen:
                    queue.append((entry[0] + 1, entry[1] - coin))
                    seen.add(entry[1] - coin)
        return -1

if __name__ == '__main__':
    solu = Solution()
    coins = [2, 5]
    amount = 11
    res = solu.coinChange2(coins, amount)
    print(res)