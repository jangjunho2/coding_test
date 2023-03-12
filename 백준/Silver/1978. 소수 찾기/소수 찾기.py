a=input()
b=list(map(int,input().split()))
c=max(b)
d=[False]*2+[True]*(c-1)
cnt=0
primes=[]

for i in range(2,c+1):
  if d[i]:
    primes.append(i)
    for j in range(i*2,c+1,i):
      d[j]=False

for k in b:
  if k in primes:
    cnt+=1

print(cnt)