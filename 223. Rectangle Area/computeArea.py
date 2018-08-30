#-*- coding: UTF-8 -*-

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        leftx = E if A < E else A
        rightx = C if C < G else G
        bottomy = B if B > F else F
        topy = D if D < H else H
        if(leftx >= rightx or bottomy >= topy):
            return (D-B)*(C-A)+(H-F)*(G-E)
        else:
            return (D-B)*(C-A)+(H-F)*(G-E)-(rightx-leftx)*(topy-bottomy)

if __name__ == '__main__':
    solu = Solution()
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    res = solu.computeArea(A, B, C, D, E, F, G, H)
    print(res)
