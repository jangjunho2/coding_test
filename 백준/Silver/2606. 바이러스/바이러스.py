import sys
from collections import deque


def bfs(start):
    result = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in net[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1
    return result


input = sys.stdin.readline


n = int(input())
m = int(input())
net = [[] for i in range(n+1)]  # 비어있는 그래프, 0번은 쓰지 않음
visited = [False]*(n+1)

# 그래프 그리기
for i in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

print(bfs(1))
# print(visited)
