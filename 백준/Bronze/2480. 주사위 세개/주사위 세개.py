a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c or a==c:
    if a==b:
        print(1000+a*100)
    elif c==b:
        print(1000+b*100)
    elif a==c:
        print(1000+c*100)
else:
    if   a<=b<=c:
        print(c*100)
    elif a<=c <=b:
        print(b*100)
    elif b<=a <=c:
        print(c*100)
    elif b<=c <=a:
        print(a*100)
    elif c<=a <=b:
        print(b*100)
    elif c<=b <=a:
        print(a*100)