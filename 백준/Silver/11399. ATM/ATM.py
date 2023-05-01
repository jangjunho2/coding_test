import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
p.sort()

result = 0
total = 0

for i in p:
    total += i
    result += total

print(result)
