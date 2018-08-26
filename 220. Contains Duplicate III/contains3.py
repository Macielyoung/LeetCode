#-*- coding: UTF-8 -*-

class Solution(object):
    # 一直遍历，挨个去比较，看看是否满足条件
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t==0 and len(nums)==len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i+j >= len(nums): break
                if abs(nums[i+j]-nums[i])<=t:
                    return True
        return False

    # bucket
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        maps = {}
        for i in range(len(nums)):
            keys = nums[i] / (t + 1)
            for ky in (keys, keys + 1, keys - 1):
                if ky in maps and i - maps[ky][0] <= k and abs(nums[i] - maps[ky][1]) <= t:
                    return True
            maps[keys] = (i, nums[i])

        return False

if __name__ == '__main__':
    solu = Solution()
    # nums = [1, 5, 9, 1, 5, 9]
    # k = 2
    # t = 3

    nums = [1, 2, 3, 1, 12, 2, 20, 7, 25, 1, 8, ]
    k = 3
    t = 5
    res = solu.containsNearbyAlmostDuplicate2(nums, k, t)
    print(res)