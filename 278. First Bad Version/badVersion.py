#-*- coding: UTF-8 -*-

class Solution:
    # 二分法
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while(left<=right):
            mid = (left+right)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

# if __name__ == '__main__':
#     solu = Solution()