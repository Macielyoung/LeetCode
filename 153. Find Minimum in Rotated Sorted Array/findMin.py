#-*- coding: UTF-8 -*-

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def middle(nums, left, right):
            if(left <= right):
                if (nums[left] <= nums[right]):
                    min = nums[left]
                else:
                    mid = (left + right) // 2
                    if (nums[mid] < nums[right]):
                        min = middle(nums, left, mid)
                    else:
                        min = middle(nums, mid+1, right)
            return min

        if not nums:
            return None
        left = 0
        right = len(nums)-1
        min = middle(nums, left, right)
        return min

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while(left < right):
            mid = (left+right)//2
            if(nums[mid] > nums[right]):
                left = mid+1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    solu = Solution()
    nums = [1]
    res = solu.findMin2(nums)
    print(res)
