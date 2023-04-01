def setPn(n):
    Pn = "I".join(["", *('O'*n), ""])
    return Pn


def check(Pn, s):
    count = 0
    for i in range(len(s)-len(Pn)+1):
        if s[i:i+len(Pn)] == Pn:
            count += 1
    return count


n = int(input())
m = int(input())
s = input()


Pn = setPn(n)


result = check(Pn, s)
print(result)
