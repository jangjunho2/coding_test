'''
    분할정복,재귀
    
'''
import sys


def cut(paper):
    # 자를 필요가 없을 경우
    if check(paper):
        return

    mid = len(paper)//2
    # 4등분하고 다시 cut
    p1 = cut([row[:mid] for row in paper[:mid]])
    p2 = cut([row[:mid] for row in paper[mid:]])
    p3 = cut([row[mid:] for row in paper[:mid]])
    p3 = cut([row[mid:] for row in paper[mid:]])


def check(paper):
    # 첫번째 색깔 찾기
    color = paper[0][0]  # 하양 or 파랑 # 0 or 1
    # 첫번쨰 색깔과 다른 색깔이 있나 비교하기
    for p in paper:
        for pp in p:
            if pp != color:
                return False
    # 전체를 확인했지만 전부 같은 색일 경우
    result.append(paper)  # 결과에 추가
    return True


def classification(result):
    white, blue = 0, 0
    for p in result:
        if p[0][0] == 0:
            white += 1
        else:
            blue += 1

    return white, blue


n = int(sys.stdin.readline().rstrip())

paper = []  # 처음 색종이
result = []  # 한가지 색을 갖는 색종이

for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    paper.append(temp)

cut(paper)

white, blue = classification(result)

print(white)
print(blue)
