a=int(input())
for i in range(a):
    b=input().split("X")
    c=[]
    d=[]
    while True:
        if "" in b:
            b.remove("")
        else:
            break
    for i in b:
        c.append(i.count("O"))
    for i in c:
        d.append(sum(range(i+1)))
    print(sum(d))
