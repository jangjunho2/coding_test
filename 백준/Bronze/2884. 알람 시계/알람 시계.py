h,m=map(int,input().split())
if m-45  >= 0:
    m-= 45
    print(h,m)
elif m-45 < 0:
    h-= 1 
    m += 15
    if h >= 0:
        print(h,m)
    else:
        h += 24
        print(h,m)