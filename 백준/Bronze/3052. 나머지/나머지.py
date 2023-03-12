a=[]
for i in range(10):
    a.append(int(input()))
# print(a)

b=[]
for k in a:
    b.append(int(k%42))
b=set(b)
print(len(b))


