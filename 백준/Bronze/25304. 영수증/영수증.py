a=int(input()) #실제금액
b=int(input()) #반복횟수

cnt=0

for i in range(b):
    c,d=map(int,(input().split()))
    cnt+=c*d

if cnt==a:
    print("Yes")
else:
    print("No")