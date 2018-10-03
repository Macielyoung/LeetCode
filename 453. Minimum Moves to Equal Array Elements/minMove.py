#-*- coding: UTF-8 -*-

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)

if __name__ == '__main__':
    solu = Solution()
    nums = [-100, 0, 100]
    res = solu.minMoves(nums)
    print(res)