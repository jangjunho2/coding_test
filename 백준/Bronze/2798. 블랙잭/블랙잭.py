a,num=map(int,input().split())
card=list(map(int,input().split()))

res=[]

for i in range(a):
    cnt=0
    cnt+=card[i]
    x=cnt #첫번쨰 카드 값 저장
    for j in range(i+1,a):
        cnt=x #첫번쨰 카드 값
        cnt+=card[j]
        y=cnt #첫번쨰 카드+두번쨰 카드 값 저장
        for k in range(j+1,a):
            cnt=y #첫번쨰 카드+두번쨰 카드 값
            cnt+=card[k]
            if cnt <= num: #수자보다 작거나 같은 경우만 저장
                res.append(cnt) #3장의 카드합 리스트에 추가


print(max(res)) #num을 넘지 않는 수만 들어있으니 가장 큰수를 출력

