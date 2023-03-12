from string import ascii_uppercase
# print(type(ascii_uppercase))
a=input() #입력
a=a.lower() #입력값 >>소문자
a=list(a) # 입력값 >>알파벳 리스트
b=[]  #빈리스트
for i in range(26):   #a~z
    b.append(a.count(("{}".format(chr(i+97)))))   #a~z 원소 몇개씩있나 카운트
    c=max(b)                   # 최댓값(제일 많은 카운트 많이된 원소 갯수)
# print(type(b),b)
# print(type(c),c)
if b.count(c)>1:     # 최댓값 두개 이상이면 ? 출력
    print("?")
else:
    print(ascii_uppercase[b.index(c)])    # 카운트 최댓값 원소 대문자로 출력
