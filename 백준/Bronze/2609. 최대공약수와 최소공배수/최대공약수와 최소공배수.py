l=list(map(int,input().split()))
a=max(l)
b=min(l)


def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

print(gcd(a,b))
print(int(a*b/gcd(a,b)))
