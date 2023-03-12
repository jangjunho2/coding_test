a=int(input())
d=[]
d2=[]
for i in range(a):
    d.append(input())

d=list(set(d))
d.sort() 
a=len(d)

for i in range(1,51):
    for j in range(a): 
        if len(d[j])==i:
            d2.append(d[j])

for i in d2:
    print(i)