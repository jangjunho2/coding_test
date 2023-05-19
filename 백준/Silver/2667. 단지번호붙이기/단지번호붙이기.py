import sys
from collections import deque
input = sys.stdin.readline


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        # 상하좌우
        for i in range(4):
            nr = v[0]+dr[i]
            nc = v[1]+dc[i]
            # 범위 내이고
            if 0 <= nc < n and 0 <= nr < n:
                # "1(집)" 이면서 방문하지 않았다면
                if city[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True  # 방문처리
                    queue.append((nr, nc))
                    cnt += 1
    homes.append(cnt)

    # 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


n = int(input())


visited = [([False]*n)for i in range(n)]
homes = []
city = []
for i in range(n):
    temp = list(map(int, input().rstrip()))
    city.append(temp)

# 탐색시작
count = 0
for i in range(n):
    for j in range(n):
        # 방문 한적 없으며, 집이라면 방문
        if not visited[i][j] and city[i][j] == 1:
            bfs(i, j)
            count += 1
print(count)
homes.sort()
for i in homes:
    print(i)
