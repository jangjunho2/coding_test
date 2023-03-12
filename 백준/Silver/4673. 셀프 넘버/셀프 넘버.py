a=[]
b=list(range(1,10000+1))

for i in range(1,10000+1):
    a.append(i+sum(map(int,list(str(i)))))
# print(a)

ans= [x for x in b if x not in a]

for i in ans:
    print(i)