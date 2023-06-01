def compare(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += a[i]
        else:
            result += '?'

    return result


n = int(input())
result = input()

for i in range(n-1):
    file_name = input()
    result = compare(result, file_name)

print(result)
