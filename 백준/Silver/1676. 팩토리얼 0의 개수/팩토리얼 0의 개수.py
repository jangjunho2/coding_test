n = int(input())

result = 1

for i in range(1, n+1):
    result *= i

count = 0

while result % 10 == 0:
    count += 1
    result //= 10

print(count)
