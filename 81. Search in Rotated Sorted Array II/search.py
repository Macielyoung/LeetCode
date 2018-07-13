#-*- coding: UTF-8 -*-

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums)-1
        bool = self.binSearch(nums, low, high, target)
        return bool

    def binSearch(self, nums, low, high, target):
        while(low < high and nums[low] == nums[high]):
            high -= 1
        while(low<=high):
            medium = (low + high) // 2
            value = nums[medium]
            # print(nums[medium])
            if(value == target or nums[low]==target or nums[high]==target): return True
            # 右半边有序或者相等
            if(value <= nums[high]):
                if(target > value and target < nums[high]):
                    # 在右半边搜索
                    return self.binSearch(nums, medium+1, high, target)
                else:
                    # 在左半边搜索
                    return self.binSearch(nums, low, medium-1, target)
            # 左半边有序或者相等
            else:
                if(target >= nums[low] and target < value):
                    # 在左半边搜索
                    return self.binSearch(nums, low, medium-1, target)
                else:
                    # 在右半边搜索
                    return self.binSearch(nums, medium+1, high, target)
        return False

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,0,1,1]
    target = 3
    bool = solu.search(nums, target)
    print(bool)