import sys

stack = []


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
    return


def top():
    try:
        print(stack[-1])
    except:
        print(-1)
    return


def size():
    print(len(stack))
    return


def pop():
    try:
        print(stack.pop())
    except:
        print(-1)
    return


def push(x):
    stack.append(x)
    return

dic={'empty':empty,'top':top,'size':size,'pop':pop}

a=int(sys.stdin.readline().rstrip())

for i in range(a):
    k = (sys.stdin.readline().rstrip())
    try:
        dic[k]()
    except:
        k=k.split()
        push(k[-1])


