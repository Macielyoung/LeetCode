#-*- coding: UTF-8 -*-

class Solution(object):
    # 时间复杂度高，使用了两层循环
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        num = len(gas)
        for i in range(num):
            remain = gas[i] - cost[i]
            if(remain < 0):
                continue
            else:
                j = i
                while(remain >= 0):
                    j = (j+1) % num
                    remain += gas[j] - cost[j]
                    if(remain < 0):
                        break
                    if(j == i and remain >= 0):
                        return i
        return -1

    # 注意规律，在最小剩余gas的下一站
    def canCompleteCircuit2(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        remain, min_gas, loc = 0, 0, 0
        num = len(gas)
        for i in range(num):
            remain += gas[i] - cost[i]
            if remain < min_gas:
                min_gas = remain
                loc = (i + 1) % num
        return loc

if __name__ == "__main__":
    solu = Solution()
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    res = solu.canCompleteCircuit2(gas, cost)
    print(res)