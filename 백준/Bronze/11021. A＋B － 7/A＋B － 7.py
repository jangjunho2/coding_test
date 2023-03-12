import sys
a=int(sys.stdin.readline().rstrip())
cnt=0
while True:
        for i in range (1,a+1):
            b,c=map(int,sys.stdin.readline().rstrip().split())
            print("Case #{}:".format(i),b+c)
            cnt+=1
        if cnt == a:
            break