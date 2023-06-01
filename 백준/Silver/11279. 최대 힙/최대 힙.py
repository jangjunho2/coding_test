import sys
import heapq

input = sys.stdin.readline
heap = []

n = int(input())
for i in range(n):
    m = int(input())
    if m == 0:
        if heap != []:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-m, m))
