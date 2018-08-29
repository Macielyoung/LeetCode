#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    # 统计次数
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = Counter(nums)
        num = len(nums) // 3
        res = []
        for key in dict.keys():
            if dict[key] > num:
                res.append(key)
        return res

    # 二赢问题
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1, num2 = nums[0], nums[0]
        count1 = count2 = 0
        res = []
        for i in range(len(nums)):
            if nums[i] == num1:
                count1 += 1
            elif nums[i] == num2:
                count2 += 1
            elif count1 == 0:
                num1 = nums[i]
                count1 += 1
            elif count2 == 0:
                num2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for i in range(len(nums)):
            if(nums[i] == num1):
                count1 += 1
            elif(nums[i] == num2):
                count2 += 1
        if(count1 > len(nums)//3):
            res.append(num1)
        if (count2 > len(nums) // 3):
            res.append(num2)
        return res

if __name__ == '__main__':
    solu = Solution()
    nums = [1,1,1,3,3,2,2,2]
    # res = solu.majorityElement(nums)

    res = solu.majorityElement2(nums)
    print(res)
