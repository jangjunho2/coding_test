from math import *
a=int(input())
for i in range(a):
    num,*score=map(int,input().split())
    mean = (sum(score))/num
    l=0
    for i in score:
        if mean<i:
            l+=1
    p=str(('%.3f'%((l/num)*100)))
    print(p+"%")
