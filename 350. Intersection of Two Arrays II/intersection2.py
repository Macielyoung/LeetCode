#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    # 修改了原数组
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for val in nums1:
            if val in nums2:
                res.append(val)
                nums2.remove(val)
        return res

    # 不改变原数组，使用Counter计数
    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 1. 使用key，value来加入元素
        # intersection = Counter(nums1) & Counter(nums2)
        # res = []
        # for key, value in intersection.items():
        #     for i in range(value):
        #         res.append(key)
        # return res

        # 2. 直接使用elements方法，返回所有元素
        intersection = Counter(nums1) & Counter(nums2)
        return list(intersection.elements())

if __name__ == '__main__':
    solu = Solution()
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2, 1]
    # res = solu.intersect(nums1, nums2)
    res2 = solu.intersect2(nums1, nums2)
    print(res2)