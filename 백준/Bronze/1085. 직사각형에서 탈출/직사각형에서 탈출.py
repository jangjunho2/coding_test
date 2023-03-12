x,y,w,h=map(int,input().split())
l=[]
l.append(x)
l.append(w-x)
l.append(y)
l.append(h-y)
print(min(l))