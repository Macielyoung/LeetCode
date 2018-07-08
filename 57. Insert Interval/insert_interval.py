#-*- coding: UTF-8 -*-
import bisect

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # 法一：插入数据，使用partition interval方法
        # if(intervals is None or len(intervals) == 0): return [newInterval]
        # intervals.append(newInterval)
        # intervals = sorted(intervals, key = lambda x: x.start)
        # m = len(intervals)
        # for i in range(m):
        #     j = i+1
        #     while(j<m):
        #         if(intervals[i].end >= intervals[j].start):
        #             if(intervals[i].end < intervals[j].end):
        #                 intervals[i].end = intervals[j].end
        #             intervals.remove(intervals[j])
        #             m -= 1
        #         else:
        #             break
        # return intervals

        # 法二：使用二分查找
        start_keys = [interval.start for interval in intervals]
        end_keys = [interval.end for interval in intervals]
        start_index = bisect.bisect_left(end_keys, newInterval.start)
        end_index = bisect.bisect_right(start_keys, newInterval.end)
        if end_index == 0:
            return [newInterval] + intervals
        elif start_index == len(intervals):
            return intervals + [newInterval]
        else:
            new = Interval(s=min(newInterval.start, intervals[start_index].start), e=max(newInterval.end, intervals[end_index - 1].end))
            return intervals[:start_index] + [new] + intervals[end_index:]

        
if __name__ == '__main__':
	intervals = []
	Inter1 = Interval(1,3)
	Inter2 = Interval(6,9)
	newInter = Interval(2,5)
	intervals.append(Inter1)
	intervals.append(Inter2)
	solu = Solution()
	result = solu.insert(intervals, newInter)
	print result[0].start