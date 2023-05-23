import sys
input = sys.stdin.readline


def dfs(n):
    visited[n] = True
    for j in graph[n]:
        if not visited[j]:
            dfs(j)


n, m = map(int, input().split())

visited = [False]*(n+1)
graph = [[] for i in range(n+1)]  # 0~n

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
