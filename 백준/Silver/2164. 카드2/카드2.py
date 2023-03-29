from collections import deque

deque = deque(range(1, int(input())+1))
# print(deque)
while True:
    if len(deque) == 1:
        print(deque[0])
        break
    elif len(deque) == 0:
        print(pop_item)
        break
    deque.popleft()  # 버리기
    pop_item = deque.popleft()  # 원소 하나뺴기
    deque.append(pop_item)
