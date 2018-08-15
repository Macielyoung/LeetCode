#-*- coding: UTF-8 -*-
import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        comp = lambda a,b : 1 if a+b>b+a else -1 if a+b<b+a else 0
        nums.sort(key=functools.cmp_to_key(comp), reverse=True)
        if nums and nums[0] == '0':
            return '0'
        return "".join(nums)

    def largestNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        longest = max([len(x) for x in nums], default=0)
        array = [x * (longest // len(x) + 1) for x in nums]
        print(array)
        nums.sort(key=lambda x: x * (longest // len(x) + 1), reverse=True)
        print(nums)
        if nums and nums[0] == '0':
            return '0'
        return ''.join(nums)

if __name__ == '__main__':
    solu = Solution()
    nums = [3,30,34,5,9]
    res = solu.largestNumber(nums)
    res1 = solu.largestNumber2(nums)
    print(res, res1)