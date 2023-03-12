s=int(input())
if s<15:
    if s==3 or s==5:
        print(1)
    elif s==6: print(2)
    elif s==8: print(2)
    elif s==9: print(3)
    elif s==10: print(2)
    elif s==11: print(3)
    elif s==12: print(4)
    elif s==13: print(3)
    elif s==14: print(4)

    else:
        print(-1)
else:
    for i in range(s//5,0,-1):
        if (s-(i*5))%3==0:
            print(i+((s-(i*5))//3))
            exit()
        if i==1:
            print(-1)
            exit()

