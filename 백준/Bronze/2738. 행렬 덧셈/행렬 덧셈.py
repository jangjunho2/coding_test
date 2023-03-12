import sys

mat1=[]
mat2=[]

m,n=map(int,sys.stdin.readline().rstrip().split())

for i in range(m):
    mat1.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(m):
    mat2.append(list(map(int, sys.stdin.readline().rstrip().split())))


for i in range(m):
    for j in range(n):
        print((mat1[i][j])+(mat2[i][j]),end=" ")
    print()

