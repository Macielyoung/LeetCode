#-*- coding: UTF-8 -*-

class Solution(object):
    # 对所有数排序，开销大
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        nums = []
        for i in range(n):
            nums += matrix[i]
        nums.sort()
        return nums[k-1]

    # 使用最大堆来实现
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0], 0, 0)]
        visited = set((0, 0))
        res = None
        while k > 0:
            res = heapq.heappop(heap)
            r, c = res[1], res[2]
            if r + 1 < m and (r + 1, c) not in visited:
                heapq.heappush(heap, (matrix[r + 1][c], r + 1, c))
                visited.add((r + 1, c))
            if c + 1 < n and (r, c + 1) not in visited:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
                visited.add((r, c + 1))
            k -= 1
        return res[0]

    def kthSmallest3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        while(l<=r):
            mid = (l+r)>>1
            high = n-1
            count = 0
            for row in range(n):
                while high>-1 and matrix[row][high]>mid:
                    high -= 1
                count += high+1
            if count >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    solu = Solution()
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    k = 8
    res = solu.kthSmallest3(matrix, k)
    print(res)