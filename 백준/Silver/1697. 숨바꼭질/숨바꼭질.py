from collections import deque


def bfs(start, target):
    visited = [False]*(100000+1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        curr, time = queue.popleft()
        if curr == target:
            return time
        for op in operation:
            next = op(curr)
            if 0 <= next <= 100000 and not visited[next]:
                queue.append((next, time+1))
                visited[next] = True


operation = [
    lambda x: x-1,
    lambda x: x+1,
    lambda x: x*2,
]

n, k = map(int, input().split())

if k <= n:
    print(n-k)
else:
    print(bfs(n, k))
