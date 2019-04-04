#-*- coding: UTF-8 -*-
import math

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if not flowerbed and n > 0:
            return False
        empty = []
        count = 0
        for index, value in enumerate(flowerbed):
            if count > 0:
                if value == 1 or value == 0 and index == len(flowerbed)-1:
                    empty.append(count)
            if value == 1:
                count = 0
            else:
                count += 1
        all_count = sum([math.ceil(i/2)-1 for i in empty])
        if all_count >= n:
            return True
        else:
            return False

if __name__ == '__main__':
    solu = Solution()
    flowerbed = [1,0,1,0,1]
    n = 1
    res = solu.canPlaceFlowers(flowerbed, n)
    print(res)