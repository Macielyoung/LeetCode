#-*- coding: UTF-8 -*-

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num1 = len(nums)
        num2 = len(set(nums))
        if num1 == num2:
            return False
        else:
            return True


if __name__ == '__main__':
    solu = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    res = solu.containsDuplicate(nums)
    print(res)