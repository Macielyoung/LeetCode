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

    # O(1)空间复杂度，且不能改变原数组
    def findKthLargest4(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minv, maxv = min(nums), max(nums)
        while(minv <= maxv):
            mid = (minv+maxv)//2
            count1 = count2 = 0
            for val in nums:
                if(val >= mid):
                    count1 += 1
                if(val > mid):
                    count2 += 1
            if(count1>=k and count2<k):
                return mid
            if(count1<k):
                maxv = mid - 1
            else:
                minv = mid + 1
        return -1

if __name__ == '__main__':
    solu = Solution()
    nums = [3,2,1,5,6,4,10,9,7]
    k = 3
    res = solu.findKthLargest4(nums, k)
    print(res)