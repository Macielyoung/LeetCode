#-*- coding: UTF-8 -*-

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for val in nums1:
            if val in nums2 and val not in res:
                res.append(val)
        return res

    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    solu = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    res = solu.intersection(nums1, nums2)
    res2 = solu.intersection2(nums1, nums2)
    print(res, res2)
