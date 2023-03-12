a,b=input().split()
a=list(a)
b=list(b)
a.reverse()
b.reverse()
A=int("".join(a))
B=int("".join(b))

print(max(A,B))

