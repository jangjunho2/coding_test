import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2  # 중간값
    if array[mid] == target:
        return mid  # 0~@ 번쨰 인덱스인지 반환
    elif array[mid] > target:  # target이 더작을떄 왼쪽탐색
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


# 입력 받기
n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()  # 리스트 a 정렬

for target in targets:
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)
