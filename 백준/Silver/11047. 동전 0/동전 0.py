# 그뤼뒤
import sys

n, k = list(map(int, sys.stdin.readline().rstrip().split()))

coins = [int(sys.stdin.readline().rstrip()) for i in range(n)]

coins.reverse()

result = 0

for coin in coins:
    result += k//coin
    k %= coin


print(result)
