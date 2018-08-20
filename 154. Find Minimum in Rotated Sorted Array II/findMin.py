#-*- coding: UTF-8 -*-

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while(left < right):
            mid = (left+right)//2
            if(nums[mid] > nums[right]):
                left = mid + 1
            else:
                if(nums[mid] != nums[right]):
                    right = mid
                else:
                    right = right - 1
        return nums[left]

if __name__ == '__main__':
    solu = Solution()
    nums = [2, 2, 2, 0, 1]
    res = solu.findMin2(nums)
    print(res)