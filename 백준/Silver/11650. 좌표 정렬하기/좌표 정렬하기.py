import sys
input=sys.stdin.readline


n=int(input())

mat=[list(map(int,input().split())) for _ in range(n)]
mat.sort(key=lambda x: (x[0], x[1])) # 

for nums in mat:
    for num in nums:
        print(num, end=" ")
    print()