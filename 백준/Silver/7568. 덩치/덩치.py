n = int(input())

people = []
dict = {}

for i in range(n):
    x, y = map(int, (input().split()))
    people.append((x, y))


weight = 0
height = 1

# "자기보다 큰 덩치의 수" + 1 = 등수
for person in people:
    rank = 1
    for other in people:
        # 자신보다 덩치 큰사람 찾기
        if person != other:
            if person[weight] < other[weight] and person[height] < other[height]:
                rank += 1
    dict[person] = rank


for person in people:
    print(dict[person], end=" ")
