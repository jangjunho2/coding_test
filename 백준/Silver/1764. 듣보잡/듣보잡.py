import sys
input = sys.stdin.readline


n, m = map(int, input().split())

people_heard = set()

result = []

for i in range(n):
    temp = input().rstrip()
    people_heard.add(temp)

for i in range(m):
    temp = input().rstrip()
    if temp in people_heard:
        result.append(temp)


result.sort()
print(len(result))
for i in result:
    print(i)
