#-*- coding: UTF-8 -*-

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if(digits[i] < 9):
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

if __name__ == '__main__':
    solu = Solution()
    digits = [2, 3, 4, 1, 1, 9]
    result = solu.plusOne(digits)
    print(result)