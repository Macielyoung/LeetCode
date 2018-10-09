#-*- coding: UTF-8 -*-

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranked_nums = sorted(nums, reverse=True)
        res = ['0']*len(nums)
        for i in range(1, len(ranked_nums)+1):
            if i == 1:
                res[nums.index(ranked_nums[i-1])] = "Gold Medal"
            elif i == 2:
                res[nums.index(ranked_nums[i-1])] = "Silver Medal"
            elif i == 3:
                res[nums.index(ranked_nums[i - 1])] = "Bronze Medal"
            else:
                res[nums.index(ranked_nums[i - 1])] = str(i)
        return res

    # 排序找出每个人的排名
    def findRelativeRanks2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return ["Gold Medal"]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return ["Gold Medal", "Silver Medal"]
            else:
                return ["Silver Medal", "Gold Medal"]
        num1 = sorted(nums)[::-1]
        dic = {num: str(i + 1) for i, num in enumerate(num1)}
        dic.update({num1[0]: "Gold Medal", num1[1]: "Silver Medal", num1[2]: "Bronze Medal"})
        return [dic[i] for i in nums]

if __name__ == '__main__':
    solu = Solution()
    nums = [2, 5]
    res = solu.findRelativeRanks(nums)
    print(res)