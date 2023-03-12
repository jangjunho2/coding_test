from string import ascii_uppercase
up = ascii_uppercase

# print(up)
cnt=0
a=input()
a=list(a)
for i in (a):
    if i in up[18]:
        ans=7
    elif i in up[19:22]:
        ans=8
    elif i in up[22:]:
        ans=9
    else:
        ans=((int(up.index(i)))//3)+2
    cnt+=ans
print(int(cnt)+len(a))

