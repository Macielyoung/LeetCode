#-*- coding: UTF-8 -*-

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        res = max(min(citations[i], i+1) for i in range(len(citations)))
        return res


if __name__ == '__main__':
    solu = Solution()
    citations = [3,0,6,1,5]
    res = solu.hIndex(citations)
    print(res)