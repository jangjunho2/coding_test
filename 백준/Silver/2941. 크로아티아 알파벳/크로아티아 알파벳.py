a=input()
b=len(a)
cnt=0
croa=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in croa:
    if i in a:
        cnt+=a.count(i)
print(b-cnt)