#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    # 计算两点之间距离
    def distanceSquare(self, A, B):
        dis = (A[0]-B[0])**2+(A[1]-B[1])**2
        return dis

    # 统计每个点到一个点的距离，数据存储形式为 {0 : {1 : [1, 2]}}, 表示为到第0个点距离为1的是第1和2个点
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        dict = {}
        for i in range(len(points)):
            value = {}
            for j in range(len(points)):
                dis = self.distanceSquare(points[i], points[j])
                if dis not in value:
                    value[dis] = [j]
                else:
                    value[dis].append(j)
            dict[i] = value
        count = 0
        for key in dict:
            for k in dict[key]:
                n = len(dict[key][k])
                count += n*(n-1)
        return count

    # 思路一致，写法更简洁
    def numberOfBoomerangs2(self, points):
        return sum(n * (n - 1) for x1, y1 in points
            for n in Counter(
                (x1 - x2) ** 2 + (y1 - y2) ** 2
                for x2, y2 in points).values())

if __name__ == '__main__':
    solu = Solution()
    points = [[0,0],[1,0],[2,0]]
    # dic = Counter((x1 - x2) ** 2 + (y1 - y2) ** 2 for x1, y1 in points for x2, y2 in points)
    # print(dic)
    res = solu.numberOfBoomerangs2(points)
    print(res)