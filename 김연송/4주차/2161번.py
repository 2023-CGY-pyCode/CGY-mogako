import sys
from collections import deque

N = int(sys.stdin.readline()) # 카드 수

queue = deque()
A = [] # 버린 카드를 저장할 배열

for i in range(1, N + 1): # 카드 순서대로 놓기
    queue.append(i)

for i in range(N - 1):
    A.append(queue.popleft()) # 제일 위 카드 버리고 배열에 저장
    queue.append(queue.popleft()) # 제일 위 값 뒤에 넣기

for i in range(len(A)):
    print(A[i], end = " ")
print(queue[0])
