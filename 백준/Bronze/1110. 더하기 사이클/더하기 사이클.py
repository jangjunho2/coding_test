a=int(input())  #입력      26
b=(a//10)+(a%10)  #일의자리와 십의자리의 합    08
k=b%10   #일의자리+십의자리 합의 일의자리 #오른쪽숫자 8
c=a%10 #일의자리 #왼쪽숫자   # 6
#새로운 숫자= c*10+k
new=c*10+k

#print(a,b,c,k,new,sep="\n")
cnt=1

while a!=new:
    b=(new//10)+(new%10)
    k=b%10
    c=new%10
    new=c*10+k
    
    cnt+=1
    
    
if a==new:
        print(cnt)


