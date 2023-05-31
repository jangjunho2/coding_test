import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = v
                queue.append(i)


graph = [[] for _ in range(n+1)]  # 0번은 쓰지않음
visited = [False]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()

for i in range(2, n+1):
    print(visited[i])
