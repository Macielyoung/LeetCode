#-*- coding: UTF-8 -*-

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = [-1] + [i for i in range(len(nums)) if nums[i]==0] + [len(nums)]
        res = max([index[i+1]-index[i]-1 for i in range(len(index)-1)])
        return res

    # 动态规划思想
    def findMaxConsecutiveOnes2(self, nums):
        for i in range(1, len(nums)):
            if nums[i]:
                nums[i] += nums[i - 1]
        return max(nums)

    # 转化为string来分割'0'
    def findMaxConsecutiveOnes3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        string = "".join(map(str, nums))
        res = max(map(len, string.split('0')))
        return res

if __name__ == '__main__':
    solu = Solution()
    nums = [1,1,0,1,1,1]
    res = solu.findMaxConsecutiveOnes3(nums)
    print(res)