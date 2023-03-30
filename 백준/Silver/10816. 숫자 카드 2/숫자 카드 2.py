import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

dic = {}

# cards에서 수를 입력받고
for card in cards:
    # 해당 키 값 이 없다면 생성
    if card not in dic:
        dic[card] = 1
    # 해당 키 값 이 있다면 값+1
    else:
        dic[card] += 1

# nums에서 들어온 숫자를 키로 넣고 접근해 값을 출력
for num in nums:
    if num not in dic:
        print(0, end=" ")
    else:
        print(dic[num], end=" ")
