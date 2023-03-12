from math import *
num=int(input())



for i in range(num):
    H,W,N=map(int,(input().split()))
    f=N%H
    if f==0:
        f=H
    f=str(f)
    b=str(ceil(N/H))
    print(f+(b.zfill(2)))

