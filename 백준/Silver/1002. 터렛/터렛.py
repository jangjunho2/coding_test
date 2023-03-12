a=int(input())

for i in range(a):
    b=list(map(int,input().split()))
    d=(((b[0] - b[3])**2 + (b[1] - b[4])**2)**(1/2)) 
    rp=b[2]+b[5]

    if d==0:  #case 6
        if b[2]==b[5]:
             print(-1)
        else: 
            print(0)
    elif d+b[5]<b[2] or d+b[2]<b[5]:  #case 5
        print(0)
    elif d+b[2]==b[5] or d+b[5]==b[2] or rp==d: #case2,3
        print(1) 
    elif rp<d: #case4
        print(0)
    elif b[2]-b[5]<d<rp or b[5]-b[2]<d<rp: #case1
        print(2)  