def solution(num):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return solution(num-1) + solution(num-2) + solution(num-3)


n = int(input())

for i in range(n):
    result = solution(int(input()))
    print(result)

