import sys

def push_front(x):
    deque.insert(0,x)

def push_back(x):
    deque.append(x)

def pop_front():
    try:
        popitem=deque.pop(0)
        print(popitem)
    except:
        print(-1)
        
def pop_back():
    try:
        popitem=deque.pop()
        print(popitem)
    except:
        print(-1)    
        
def size():
    print(len(deque))

def empty():
    if len(deque)==0:
        print(1)
    else:
        print(0)

def front():
    try:
        print(deque[0])
    except:
        print(-1)

def back():
    try:
        print(deque[-1])
    except:
        print(-1)
dic={"push_front":push_front,
     "push_back":push_back,
     "pop_front":pop_front,
     "pop_back":pop_back,
     "size":size,
     "empty":empty,
     "front":front,
     "back":back
     }


deque=[]




k=int(sys.stdin.readline())

for i in range(k):
    a=list(sys.stdin.readline().split())
    try:
        dic[a[0]](a[1]) #딕셔너리에있는 함수 실행
    except:
        dic[a[0]]()