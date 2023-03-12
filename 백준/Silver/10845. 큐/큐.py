import sys
queue=[]

def empty():
  if len(queue)==0:
    print(1)
  else:
    print(0)

def back():
  try:
    print(queue[-1])
  except:
    print(-1)

def front():
  try:
    print(queue[0])
  except:
    print(-1)

def size():
  print(len(queue))

def pop():
  try:
    b=queue[0]
    del queue[0]
    print(b)
  except:
    print(-1)
  
def push(x):
  queue.append(x)
###

a=int(sys.stdin.readline().rstrip())

for i in range(a):
  k=sys.stdin.readline().rstrip()
  if k=='empty':
    empty()
  elif k=='back':
    back()
  elif k=='front':
    front()
  elif k=='size':
    size()
  elif k=='pop':
    pop()
  else:
    b=k.split()
    push(b[-1])

  

