n = int(input())
m = list(input())

nums = [ord(i)-96 for i in m]

total = 0

for i in range(n):
    total += nums[i] * (31**i)

print(total)
