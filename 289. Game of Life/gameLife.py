#-*- coding: UTF-8 -*-

class Solution:
    # 只需要记录改变的位即可
    # 如果当前位为1，周围少于2个或超过3个活着，需要改变
    # 如果当前位为0，周围有三个活着，需要改变
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        changeList = set()

        def judge(x, y):
            live = 0
            # 统计周围八格的方法，比较简单，👍
            for spot in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                newx, newy = x + spot[0], y + spot[1]
                if newx < 0 or newx >= len(board) or newy < 0 or newy >= len(board[0]): continue
                if board[newx][newy] == 1: live += 1
            if live < 2:
                if board[x][y] == 1: changeList.add((x, y))
            elif live == 3:
                if board[x][y] == 0: changeList.add((x, y))
            elif live > 3:
                if board[x][y] == 1: changeList.add((x, y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                judge(i, j)

        for pair in changeList:
            x, y = pair[0], pair[1]
            board[x][y] = 1 if board[x][y] == 0 else 0

if __name__ == '__main__':
    solu = Solution()
    board = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1],
             [0, 0, 0]]
    solu.gameOfLife(board)
    print(board)