import sys
input = sys.stdin.readline

n = int(input())


people = []
for i in range(n):
    a, b = input().split()
    people.append([int(a), b])

people.sort(key=lambda x: x[0])
'''
Python에서 기본적으로 지원하는 정렬 알고리즘은 Tim Sort는 Stable 합니다.

(Tim sort는 Insertion Sort와 Merge Sort를 Hybrid 하여 구현한 알고리즘으로 Insertion과 Merge 모두 Stable Sort Algorithm 입니다.)

동일한 값을 갖는 경우 순서가 보장되는 Stable Algorithm이니 그냥 나이 순으로 정렬하기만 해도 됩니다.'''
for person in people:
    print(" ".join(map(str, person)))
