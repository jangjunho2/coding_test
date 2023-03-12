a=int(input())
for i in range(a):
    b=list(input())
    lenB=len(b)
    cnt=0
    for j in range(lenB):
        if cnt<0:# ) 가 ( 보다 먼저 온 경우는 절대 VSP 만족 불가
            break
        elif b[j]=='(': # ) 가 나와줘하므로 cnt +=1
            cnt+=1
        else:  # ) 가 나오면 cnt-=1
            cnt-=1
    if cnt==0:   #모든 사이클이 돌고 같은 경우 VSP
        print("YES")
    else:       #모든 사이클이 돌았지만 마지막 ( ( ) ) ) 같은 경우 위에서 잡아내지 못함 VSP가 아님
        print("NO")
        
        
    