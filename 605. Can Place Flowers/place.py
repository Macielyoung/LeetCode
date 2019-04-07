#-*- coding: UTF-8 -*-
import math

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        pos, count = 0, 0
        length = len(flowerbed)
        while pos < length:
            if (flowerbed[pos]==0)and(pos==0 or flowerbed[pos-1]==0)and(pos==length-1 or flowerbed[pos+1]==0):
                flowerbed[pos] = 1
                count += 1
            pos += 1
        return count >= n
    
    def canPlaceFlowers2(self, flowerbed, n):
        pos, count = 0, 0
        length = len(flowerbed)
        while pos < length:
            if (flowerbed[pos]==0)and(pos==0 or flowerbed[pos-1]==0)and(pos==length-1 or flowerbed[pos+1]==0):
                flowerbed[pos] = 1
                pos += 1
                count += 1
            if count >= n:
                return True
            pos += 1
        return False

if __name__ == '__main__':
    solu = Solution()
    flowerbed = [0,0,1,0,1]
    n = 1
    res = solu.canPlaceFlowers2(flowerbed, n)
    print(res)