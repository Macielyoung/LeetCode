#-*- coding: UTF-8 -*-

class Solution:
    # 超时，需要遍历整个数组
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num = len(nums)
        if(k>=num-1):
            num2 = len(set(nums))
            res = True if num > num2 else False
            return res
        else:
            for i in range(num):
                if(i<num-k):
                    if len(set(nums[i:i+k+1])) < k+1:
                        return True
                else:
                    if len(set(nums[i:])) < len(nums[i:]):
                        return True
        return False

    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            else:
                if i - dict[nums[i]] <= k:
                    return True
                else:
                    dict[nums[i]] = i
        return False

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    res = solu.containsNearbyDuplicate2(nums, k)
    print(res)