from collections import deque


def dfs(graph, v, visited):
    if visited[v] == False:  # 방문한적 없는 노드 방문하면 정렬해주기
        graph[v].sort()
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visted):
    queue = deque([v])
    visted[v] = True
    while queue:
        v = queue.popleft()
        # graph[v].sort() #꺼낸다음에 정렬해줄 필요 없음 DFS에서 이미 정렬함
        print(v, end=" ")
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visted[i] = True


n, m, v = map(int, input().split())

graph = [[]for _ in range(n+1)]  # 0번은 버림
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)


'''
i j를 입력 받으면 i-j 를 연결하는 간선이 생김
graph[i] 에 가서 j를 추가하고
graph[j] 에 가서 1을 추가함
'''
for i in range(m):  # m번 입력받기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

dfs(graph, v, visited_dfs)
print()  # 줄 바꿈
bfs(graph, v, visited_bfs)
