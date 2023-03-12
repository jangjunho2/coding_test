num=int(input())
for i in range(1000000+1):
   temp=str(i)
   for j in range(len(temp)):
      i+=int(temp[j])
   if i==num:
      print(int(temp))
      exit()
print(0)
