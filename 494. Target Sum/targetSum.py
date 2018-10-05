#-*- coding: UTF-8 -*-

class Solution(object):
    # 遍历所有情况，最后查看dic中是否存在结果为S的情况
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

    def findTargetSumWays2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        memo = {}
        return self.dfs(nums, S, memo)

    def dfs(self, nums, S, memo):
        if tuple(nums + [S]) in memo:
            return memo[tuple(nums + [S])]
        if not nums:
            if S == 0:
                return 1
            return 0
        cnt = 0
        cnt += self.dfs(nums[1:], S - nums[0], memo)
        cnt += self.dfs(nums[1:], S + nums[0], memo)
        memo[tuple(nums + [S])] = cnt
        return cnt

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    res = solu.findTargetSumWays2(nums, S)
    print(res)