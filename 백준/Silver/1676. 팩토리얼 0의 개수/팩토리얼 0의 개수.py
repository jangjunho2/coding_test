n = int(input())

result = 1

for i in range(1, n+1):
    result *= i
result = list(str(result))

count = 0

for i in reversed(result):
    if i == '0':
        count += 1
    else:
        print(count)
        break
