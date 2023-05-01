sites = {}

n, m = map(int, input().split())

for i in range(n):
    temp = input().split()
    sites[temp[0]] = temp[1]

for i in range(m):
    site = input()
    print(sites[site])
