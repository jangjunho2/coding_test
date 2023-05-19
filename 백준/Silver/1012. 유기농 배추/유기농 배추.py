from collections import deque
import sys
input = sys.stdin.readline


n = int(input())


def put_cabbage(p_row, p_col):
    field[p_row][p_col] = 1


def find_cabbage():

    def looking():
        count = 0
        for i in range(row):
            for j in range(col):
                if field[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
                    count += 1
        return count

    def bfs(crow, ccol):
        queue = deque([(crow, ccol)])
        visited[crow][ccol] = True
        while queue:
            v = queue.popleft()
            for i in range(4):
                nrow = v[0]+drow[i]
                ncol = v[1]+dcol[i]
                # 범위 내 체크
                if 0 <= nrow < row and 0 <= ncol < col:
                    # 배추 체크
                    if not visited[nrow][ncol] and field[nrow][ncol]:
                        visited[nrow][ncol] = True
                        queue.append((nrow, ncol))

    visited = [[False]*col for i in range(row)]
    result = looking()
    return result


# 상하좌우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


for i in range(n):
    col, row, c = map(int, input().split())  # 가로 세로 배추

    field = [[0]*col for i in range(row)]

    for i in range(c):
        p_col, p_row = list(map(int, input().split()))
        put_cabbage(p_row, p_col)
    print(find_cabbage())
