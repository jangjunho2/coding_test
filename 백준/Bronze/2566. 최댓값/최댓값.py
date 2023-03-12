num=[]
for i in range(9):
        num.append(list(map(int, input().split())))

temp=num
temp=sum(num,[])
max=max(temp)
row=(temp.index(max))//9
col=(temp.index(max))%9
print(max)
print(row+1,col+1)
