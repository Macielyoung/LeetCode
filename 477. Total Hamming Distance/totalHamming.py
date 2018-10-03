#-*- coding: UTF-8 -*-

class Solution(object):
    # 超时，时间复杂度O(n^2)
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==1:
            return 0
        sum = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                count = (bin(nums[i]^nums[j])[2:]).count('1')
                sum += count
        return sum

    # Time : O(n), Space : O(1), 统计每一位0，1的数量
    def totalHammingDistance2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==1:
            return 0
        n = len(nums)
        maxx = max(nums)
        ans = 0
        m = 1
        while m <= maxx:
            ones = 0
            for num in nums:
                if m & num:
                    ones += 1
            zeros = n - ones
            ans += ones * zeros
            m <<= 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [14, 4, 2]
    res = solu.totalHammingDistance2(nums)
    print(res)