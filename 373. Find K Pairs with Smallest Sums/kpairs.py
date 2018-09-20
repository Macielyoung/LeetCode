#-*- coding: UTF-8 -*-
import heapq

class Solution(object):
    # 排序(内存溢出，空间复杂度高了)
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pairs.append([nums1[i], nums2[j]])
        pairs.sort(key=lambda x:x[0]+x[1])
        res = pairs[:k]
        return res

    # 堆排序
    def kSmallestPairs3(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: return []
        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            # 加入当前元素的下一行元素，用于和当前元素同一行的元素来比较
            if j + 1 < n: heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res

    # 类似于m*n的矩阵，每行元素逐渐增大，每列元素也逐渐增大，求矩阵中前k小元素
    # def kSmallestPairs2(self, nums1, nums2, k):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """

if __name__ == '__main__':
    solu = Solution()
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    res = solu.kSmallestPairs3(nums1, nums2, k)
    print(res)
