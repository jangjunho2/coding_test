import sys
input = sys.stdin.readline


n, m = map(int, input().split())

pocketmons_num = {}
pocketmons_name = {}

for i in range(n):
    temp = input().rstrip()
    pocketmons_num[i+1] = temp
    pocketmons_name[temp] = i+1

for i in range(m):
    temp = input().rstrip()
    if temp.isdigit():
        print(pocketmons_num[int(temp)])
    else:
        print(pocketmons_name[temp])
