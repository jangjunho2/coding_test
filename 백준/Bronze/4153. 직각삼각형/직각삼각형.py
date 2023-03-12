while(1):
    a,b,c=map(int,input().split())
    k=max(a,b,c)
    if a==0 & b==0 & c==0:
        break
    elif k*k*2==(a**2)+(b**2)+(c**2):
        print("right")
    else:
        print("wrong")