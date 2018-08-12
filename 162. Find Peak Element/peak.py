#-*- coding: UTF-8 -*-

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        if num==0:
            return None
        if num==1:
            return 0
        if num==2:
            if(nums[0]>nums[1]):
                return 0
            else:
                return 1
        for i in range(num):
            if(i==0):
                if(nums[i]>nums[i+1]):
                    return i
            elif(i==num-1):
                if(nums[i]>nums[i-1]):
                    return num-1
            else:
                if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                    return i

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3]
    res = solu.findPeakElement(nums)
    print(res)
