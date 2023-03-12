from collections import deque
import sys

input=sys.stdin.readline
n,k=map(int,input().split())

q=deque()
ans=[]

for i in range(n):
    q.append(i+1)

while(len(q)>0):
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

ans=str(ans)
ans=ans.replace('[','<')
ans=ans.replace(']','>')

print(ans)

