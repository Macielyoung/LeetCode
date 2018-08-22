#-*- coding: UTF-8 -*-

class Solution:
    # 超时
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def prime(m):
            if(m==0 or m==1):
                return False
            sqrt = int(m**0.5)+1
            for i in range(2, sqrt):
                if(m % i == 0):
                    return False
            return True
        # count = 0
        if (n == 0):
            return 0
        dp = [0 for i in range(n)]
        for i in range(1, n):
            if(prime(i)):
                dp[i] = dp[i-1]+1
            else:
                dp[i] = dp[i-1]
        # for i in range(n+1):
        #     if(prime(i)):
        #         count += 1
        return dp[-1]

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        flags = [1] * n
        flags[0] = flags[1] = 0
        for i in range(2, int(n**0.5)+1):
            if(flags[i] == 1):
                # 必须要指定迭代的数量
                flags[i*i:n:i] = [0] * ((n-1-i*i)//i+1)
        return sum(flags)

if __name__ == '__main__':
    solu = Solution()
    res = solu.countPrimes2(9)
    print(res)