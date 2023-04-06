import sys

n = int(input())

for i in range(n):
    total, target = map(int, sys.stdin.readline().rstrip().split())  # 종이의 수, 찾는 종이
    # 종이들 중요도 적힌 리스트
    papers = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0  # 출력한 종이 수
    while True:
        if max(papers) == papers[0]:  # 맨 앞에 있는게 max가 맞다면? 출력
            papers.pop(0)
            count += 1
            target -= 1
            # 출력한 대상이 타겟이라면 ?
            if target == -1:
                print(count)
                break
        else:
            # 맨 앞에 있는 수가 max가 아니라면?
            popitem = papers.pop(0)
            papers.append(popitem)
            # 원하는 출력물이 앞으로 한칸 당겨짐
            target -= 1
            # 만약 앞으로 한칸 당겨서 -1번쨰가 된다면? 맨뒤로 보냄
            if target == -1:
                target = len(papers)-1
