coins = [500, 100, 50, 10, 5, 1]

n = int(input())

result = 1000-n

cnt = 0

for coin in coins:
    if result == 0:
        break
    cnt += result//coin
    result %= coin

print(cnt)
