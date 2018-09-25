#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    # 使用生成表达式超时(O(n))，使用set求差集可以
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        distribution = Counter(nums).keys()
        raw = set(range(1, len(nums)+1))
        res = list(raw.difference(set(distribution)))
        return res

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    solu = Solution()
    nums = [4,3,2,7,8,2,3,1]
    res = solu.findDisappearedNumbers2(nums)
    print(res)