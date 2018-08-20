#-*- coding: UTF-8 -*-
import re

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        nums1 = [int(i) for i in version1.split('.')]
        nums2 = [int(i) for i in version2.split('.')]
        print(nums1, nums2)
        l1 = len(nums1)
        l2 = len(nums2)
        i, j = 0, 0
        for i in range(max(l1, l2)):
            v1 = nums1[i] if i < l1 else 0
            v2 = nums2[i] if i < l2 else 0
            if(v1 > v2):
                return 1
            if(v1 < v2):
                return -1
        return 0

if __name__ == '__main__':
    solu = Solution()
    version1 = "1.2"
    version2 = "1.10"
    res = solu.compareVersion(version1, version2)
    print(res)