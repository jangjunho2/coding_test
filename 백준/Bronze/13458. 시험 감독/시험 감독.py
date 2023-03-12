n=int(input())   #시험장수
a=list(map(int,input().split()))   #각 시험장의 응시자수
b,c=map(int,input().split())
from math import *
#####
chong=n
boo=0
for i in a:
    if i-b>0:
        boo+= (ceil((i-b)/c)) #부감독관 수
    else:
        pass
print(boo+chong)
