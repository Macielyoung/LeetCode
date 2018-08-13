#-*- coding: UTF-8 -*-

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return []
        left, right = 0, len(numbers)-1
        while(left < right):
            if(numbers[left]+numbers[right]==target):
                return [left+1, right+1]
            elif(numbers[left]+numbers[right]>target):
                right -= 1
            else:
                left += 1
        return []

if __name__ == '__main__':
    solu = Solution()
    numbers = [2,7,11,15,20,25]
    target = 31
    res = solu.twoSum(numbers, target)
    print(res)