#-*- coding: UTF-8 -*-


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num = len(nums)
        # if(num == 0):
        #     return 0
        # cursor = nums[0]
        # count = 0
        # i=0
        # while(i<num):
        #     if(nums[i] == cursor):
        #         count += 1
        #         if (count > 2):
        #             del nums[i - 1]
        #             num -= 1
        #         else:
        #             i += 1
        #     else:
        #         cursor = nums[i]
        #         count = 1
        #         i += 1
        # return num

        length = len(nums)
        i = 0
        while i + 2 < length:
            # 仅仅考虑后两位元素是否和当前元素相同即可
            if nums[i + 2] == nums[i]:
                del nums[i + 2]
                length = length - 1
            else:
                i = i + 1

        return length

if __name__ == '__main__':
    solu = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    res = solu.removeDuplicates(nums)
    print(res)
    print(nums)