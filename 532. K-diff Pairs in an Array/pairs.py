#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    # 时间复杂度O(n^2)
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[j]-nums[i]) == k:
                    if (nums[i], nums[j]) not in res and (nums[j], nums[i]) not in res:
                        res.append((nums[i], nums[j]))
        return len(res)

    def findPairs2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        dict = Counter(nums)
        res = 0
        for val in dict:
            if k > 0 and val+k in dict or k==0 and dict[val] > 1:
                res += 1
        return res


if __name__ == '__main__':
    solu = Solution()
    nums = [1,1,1,2,1]
    k = 1
    res = solu.findPairs2(nums, k)
    print(res)