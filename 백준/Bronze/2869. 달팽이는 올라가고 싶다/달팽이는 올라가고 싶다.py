from  math import *
a, b, c = map(int, input().split())  #하루 오르는 양 , 미끄러지는 양, 총 높이

#전체-마지막날 오르는양 = last

#아침이 되었을떄 last 만큼 올라와있어야함
#(아침-저녁) * 일수 >= last


last=c-a
tday=ceil(last/(a-b))

print(tday+1)