#-*- coding: UTF-8 -*-

class Solution(object):
    # 超时
    def nextGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        newNums = nums*2
        for i in range(len(nums)):
            flag = 1
            for j in range(i+1, len(newNums)):
                if newNums[j] > nums[i]:
                    res.append(newNums[j])
                    flag = 0
                    break
            if flag:
                res.append(-1)
        return res

    def nextGreaterElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        prev_max_right = []
        for j in range(2 * n - 2, -1, -1):
            i = min(j - n, j)
            if nums[i] < nums[i + 1]:
                res[i] = nums[i + 1]
                prev_max_right.append(nums[i + 1])
            else:
                max_right = -1
                while prev_max_right and prev_max_right[-1] <= nums[i]:
                    prev_max_right.pop()
                if prev_max_right:
                    max_right = prev_max_right[-1]
                else:
                    prev_max_right.append(nums[i])
                res[i] = max_right
        return res

    def nextGreaterElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            stack.append(nums[i])
        return ret

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,1,4,3,5,2,7]
    res = solu.nextGreaterElement3(nums)
    print(res)
