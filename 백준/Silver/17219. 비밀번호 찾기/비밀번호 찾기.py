import sys

sites = {}

n, m = map(int, sys.stdin.readline().rstrip().split())

for i in range(n):
    temp = sys.stdin.readline().rstrip().split()
    sites[temp[0]] = temp[1]

for i in range(m):
    site = sys.stdin.readline().rstrip()
    print(sites[site])
