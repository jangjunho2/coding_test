def setPn(n):
    Pn = "I".join(["", *('O'*n), ""])
    return Pn


n = int(input())
m = int(input())
s = input()


Pn = setPn(n)
lst = [s[i:i+len(Pn)] for i in range(m-len(Pn)+1)]

count = 0

for i in lst:
    if i == Pn:
        count += 1

print(count)
