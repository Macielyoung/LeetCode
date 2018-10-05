#-*- coding: UTF-8 -*-

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        timeDuration = [timeSeries[i+1]-timeSeries[i] for i in range(len(timeSeries)-1)]
        for i in range(len(timeDuration)):
            if timeDuration[i]>duration:
                timeDuration[i] = duration
        return sum(timeDuration)+duration

if __name__ == '__main__':
    solu = Solution()
    timeSeries = [1]
    duration = 2
    res = solu.findPoisonedDuration(timeSeries, duration)
    print(res)