import math

class Solution:
    def countPrimes(self, n: int) -> int:
        num_list = [True for _ in range(n)]

        for i in range(2, int(pow(n, 0.5)) + 1):
            if num_list[i]:  # 如果i为质数(不是任何质数的倍数)
                for j in range(i * i, n, i):
                    num_list[j] = False

        ans = 0
        for i in range(2, n):
            if num_list[i]:
                ans += 1
        return ans

    def countPrimes2(self, n: int) -> int:
        prime_list = []
        for c in range(2, n):
            flag = 0
            for i in prime_list:
                if c % i == 0:
                    flag = 1
                    break
            if flag == 0:
                prime_list.append(c)
        return len(prime_list)

    def countPrimes3(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        if n == 3:
            return 1
        if self.judgePrime(n-1):
            return 1 + self.countPrimes(n-1)
        else:
            return self.countPrimes(n-1)
    
    def judgePrime(self, n):
        flag = 1
        for i in range(2, math.ceil(n ** 0.5)+1):
            if n % i == 0:
                flag = 0
                return flag
        return flag

if __name__ == "__main__":
    n = 10
    s = Solution()
    p = s.judgePrime(4)
    print(p)
    res = s.countPrimes(n)
    print(res)