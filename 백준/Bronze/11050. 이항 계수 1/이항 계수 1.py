def fact(n):
    temp=1
    for i in range(n):
        temp*=(i+1)
    return temp

a=list(map(int,input().split()))

res=fact(a[0]) / ((fact(a[0]-a[1])) * fact(a[1]))

print(int(res))