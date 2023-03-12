a=input()
for i in range(int(a)):
    b=input().split()
    c =list(b[1])
    for j in c:
        print(j*int(b[0]),end="")
    print("")
