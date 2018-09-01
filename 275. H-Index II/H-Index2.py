#-*- coding: UTF-8 -*-

class Solution(object):
    # O(n)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for loc, val in enumerate(citations[::-1]):
            if loc+1>val:
                return loc
        return len(citations)

    # O(n)
    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        res = max(min(citations[i], len(citations)-i) for i in range(len(citations)))
        return res

    # O(logn)
    def hIndex3(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l, r, out = 0, len(citations) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            if len(citations) - mid <= citations[mid]:
                out, r = len(citations) - mid, r - 1
            else:
                l = mid + 1
        return out

if __name__ == '__main__':
    solu = Solution()
    citations = [0,1,3,5,6]
    citations2 = [3,4,5,8,10]
    citations3 = [3,3,5,8,25]
    res = solu.hIndex3(citations2)
    print(res)