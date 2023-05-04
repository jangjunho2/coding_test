# 그뤼뒤
import sys

n, k = list(map(int, sys.stdin.readline().split()))

coins = [int(sys.stdin.readline()) for i in range(n)]

result = 0

for coin in coins[::-1]:
    result += k//coin
    k %= coin


print(result)
