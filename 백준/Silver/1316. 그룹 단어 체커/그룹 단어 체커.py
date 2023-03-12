cnt=0
a=int(input())
for i in range(a):
    dic=[]  
    wrong=0
    b=list(input())
    for j in range(len(b)):
        if b[j] in dic:
            wrong+=1
            break
        elif j==0:
            continue
        elif b[j]==b[j-1]:
            continue
        else:
            dic.append(b[j-1])
    if wrong>=1:
        pass
    else:
        cnt+=1 
print(cnt)
