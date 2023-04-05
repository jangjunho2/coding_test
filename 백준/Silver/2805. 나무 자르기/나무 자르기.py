def binary_seacrch(array, target, start, end):
    while True:
        if start > end:
            return result
        mid = (start+end)//2
        total = 0
        for i in range(n):
            if trees[i] > mid:  # 트리 > 설정한 값 이면?
                total += trees[i]-mid
                # print(total)
        if target > total:  # 목표한 값 보다 적은 경우  # 왼쪽 탐색
            end = mid-1
        else:  # 오른쪽 탐색 #목표한 값 이랑 같거나 많은 경우
            result = mid
            start = mid+1


n, m = map(int, input().split())
trees = list(map(int, input().split()))


result = binary_seacrch(trees, m, 0, max(trees))

print(result)
