import sys
input = sys.stdin.readline

n = int(input())

stairs = []

for _ in range(n):
    stairs.append(int(input()))

dp = [0]*n

dp[0] = stairs[0]
if n == 1:
    print(dp[0])
    sys.exit()
dp[1] = stairs[0]+stairs[1]

if n > 3:
    dp[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])

for i in range(3, n):
    dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

print(dp[n-1])
