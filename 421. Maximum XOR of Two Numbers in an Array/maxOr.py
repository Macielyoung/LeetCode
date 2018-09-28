#-*- coding: UTF-8 -*-

class Solution(object):
    # 超时 O(n^2)
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                xor = nums[i] ^ nums[j]
                if xor > max_or:
                    max_or = xor
        return max_or

    def findMaximumXOR2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # answer = 0
        # for i in range(32)[::-1]:
        #     answer <<= 1
        #     prefixes = {num >> i for num in nums}
        #     answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        # return answer
        # 易懂版本
        mx, mask = 0, 0
        for i in range(31, -1, -1):
            possible_mx = mx | 1 << i
            mask = mask | 1 << i
            bits = set()
            for num in nums:
                bits.add(num & mask)
            for bit in bits:
                if bit ^ possible_mx in bits:
                    mx = possible_mx
                    break
        return mx

if __name__ == '__main__':
    solu = Solution()
    nums = [3, 10, 5, 25, 2, 8]
    res = solu.findMaximumXOR2(nums)
    print(res)