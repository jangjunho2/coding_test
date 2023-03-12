a,b=map(int,input().split())
c=[False]*2 + [True]*(b-1)
primes=[]
for i in range(2,b+1):
  if c[i]:
    primes.append(i)
    for j in range(2*i,b+1,i):
      c[j]=False


for k in primes:
  if k>=a:
    print(k)

