#-*- coding: UTF-8 -*-

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        m = len(intervals)
        if (intervals is None or m == 0): return []
        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(m):
            j = i + 1
            while (j < m):
                if (intervals[i].end >= intervals[j].start):
                    if (intervals[i].end < intervals[j].end):
                        intervals[i].end = intervals[j].end
                    intervals.remove(intervals[j])
                    m -= 1
                else:
                    break
        return intervals
        
if __name__ == '__main__':
    intervals = []
    inter1 = Interval(1,3)
    inter2 = Interval(6,9)
    inter3 = Interval(2,5)
    intervals.append(inter1)
    intervals.append(inter2)
    intervals.append(inter3)
    solu = Solution()
    result = solu.merge(intervals)
    print result[0].start