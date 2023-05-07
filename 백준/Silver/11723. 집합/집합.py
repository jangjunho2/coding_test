# https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline

my_set = set()


def add(x):
    my_set.add(x)


def remove(x):
    my_set.discard(x)  # remove 쓰면 x가 없을때 에러, discard 쓰면 x가 없을때 무시됨


def check(x):
    if x in my_set:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in my_set:
        remove(x)
    else:
        add(x)


def all():
    my_set.update(range(1, 20+1))


def empty():
    my_set.clear()


func = {"add": add, "remove": remove, "check": check,
        "toggle": toggle, "all": all, "empty": empty}

n = int(input())

for i in range(n):
    btn = input().rstrip().split()
    if len(btn) == 1:
        func[btn[0]]()
    else:
        func[btn[0]](int(btn[1]))
