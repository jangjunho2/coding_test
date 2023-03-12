import sys
input=sys.stdin.readline
nums=[]

a=int(input())
for i in range(a):
    nums.append(int(input()))
nums.sort()
for i in nums:
    print(i)