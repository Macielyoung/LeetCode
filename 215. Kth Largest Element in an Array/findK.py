#-*- coding: UTF-8 -*-
import heapq

class Solution:
    # 排序
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]

    # 最小堆
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for i in range(k):
            res = heapq.heappop(heap)
        return -res

    # 快排思想
    def findKthLargest3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = 0, len(nums)
        while(low < high):
            pivot = nums[low]
            i, j = low, high-1
            while(i<=j):
                while(i<=j and nums[i]>=pivot):
                    i += 1
                while(i<=j and nums[j]<pivot):
                    j -= 1
                if(i<j):
                    nums[i], nums[j] = nums[j], nums[i]
            nums[low], nums[j] = nums[j], nums[low]
            if(j==k-1):
                return nums[j]
            elif(j<k-1):
                low = j+1
            else:
                high = j

if __name__ == '__main__':
    solu = Solution()
    nums = [3,2,1,5,6,4,10,9,7]
    k = 5
    res = solu.findKthLargest3(nums, k)
    print(res)