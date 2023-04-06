import sys


def binary_search(lines, target, start, end):
    while True:
        if start > end:
            return result
        mid = (start+end)//2
        count = 0
        for i in range(len(lines)):
            pass
            count += lines[i] // mid
        # 모자란 경우 #왼쪽 탐색
        if count < target:
            end = mid-1
        # 오른쪽 탐색
        else:
            result = mid
            start = mid+1


# 가지고 있는 랜선의 개수 K , 필요한 랜선의 수 N
k, n = map(int, sys.stdin.readline().rstrip().split())

lines = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

print(binary_search(lines, n, 1, max(lines)))
