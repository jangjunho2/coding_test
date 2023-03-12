a=int(input())
for i in range(2,10000000+1):
  if a%i==0:
    while a%i==0:
      a=a/i
      print(i)
      