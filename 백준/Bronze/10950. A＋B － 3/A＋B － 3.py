index=int(input())
while index >=1:
     b,c=map(int,input().split())
     print(b+c)
     index -=1
     if index == 0:
         break