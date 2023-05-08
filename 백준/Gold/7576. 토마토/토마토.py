import sys
from collections import deque
input = sys.stdin.readline


def search_tomato_1() -> list:
    tomatoes_1 = []
    for i, row in enumerate(box):
        for j, col in enumerate(row):
            if col == 1:
                tomatoes_1.append([i, j])
    return tomatoes_1


def search_tomato_0() -> bool:
    tomatoes_1 = []
    for i, row in enumerate(box):
        for j, col in enumerate(row):
            if col == 0:
                return True
    return False


def bfs() -> int:
    tomatoes_1 = search_tomato_1()
    # print(tomatoes_1)
    queue = deque(tomatoes_1)
    result = 0
    while queue:
        v = queue.popleft()
        for i in range(4):
            nrow = (v[0]+drow[i])
            ncol = (v[1]+dcol[i])
            # 범위 이내
            if 0 <= nrow < row and 0 <= ncol < col:
                # 익지않은(0) 이라면
                if box[nrow][ncol] == 0:
                    box[nrow][ncol] = box[v[0]][v[1]]+1
                    queue.append([nrow, ncol])
                    result = box[v[0]][v[1]]
    if search_tomato_0():
        return -1
    return result


col, row = map(int, input().split())


box = [list(map(int, input().split())) for i in range(row)]

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

print(bfs())
# print(box)
