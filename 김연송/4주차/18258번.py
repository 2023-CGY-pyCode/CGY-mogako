import sys
from collections import deque

N = int(sys.stdin.readline()) # 명령의 수
queue = deque()

for i in range(N):
    X = list(sys.stdin.readline().split())

    if X[0] == "push":
        queue.append(X[1])

    elif X[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif X[0] == "size":
        print(len(queue))

    elif X[0] == "empty":
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
        
    elif X[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif X[0] == "back":
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[len(queue) - 1])
