#-*- coding: UTF-8 -*-

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for val in findNums:
            index = nums.index(val)
            flag = 1
            for i in range(index+1, len(nums)):
                if(nums[i]>val):
                    res.append(nums[i])
                    flag = 0
                    break
            if flag:
                res.append(-1)
        return res

    def nextGreaterElement2(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1] < nums[i]:
                dict[stack.pop()] = nums[i]
            stack.append(nums[i])
        res = []
        for i in range(len(findNums)):
            if findNums[i] in dict:
                res.append(dict[findNums[i]])
            else:
                res.append(-1)
        return res

if __name__ == '__main__':
    solu = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,6,5,4,2]
    # res = solu.nextGreaterElement(nums1, nums2)
    res = solu.nextGreaterElement2(nums1, nums2)
    print(res)
