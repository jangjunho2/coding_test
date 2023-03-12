a=int(input())
b=int(input())
c=int(input())
k=a*b*c
# print(k)
k=str(k)
# print(type(k))
for i in range(10):
    print(k.count("{}".format(i)))

