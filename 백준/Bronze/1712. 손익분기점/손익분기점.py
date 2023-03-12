from math import *
a,b,c=map(int,input().split())
if b>=c:
    print(-1)
else:
    print(floor((a/(c-b))+1))