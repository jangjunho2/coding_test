import sys
a=int(input())
cnt=0
while True:
    b,c=map(int,sys.stdin.readline().rstrip().split())
    print(b+c)
    cnt+=1
    if cnt == a:
        break
