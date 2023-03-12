a=int(input())

for n in range(100000000):
  if a<=3*n*(n+1)+1:
    print(n+1)
    exit()  
    