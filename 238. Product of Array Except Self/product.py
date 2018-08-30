#-*- coding: UTF-8 -*-

class Solution:
    # 不能使用除法，不符合要求
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        accumulation = 1
        for i in range(len(nums)):
            accumulation *= nums[i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = accumulation // nums[i]
        return res

    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,4]
    res = solu.productExceptSelf2(nums)
    print(res)