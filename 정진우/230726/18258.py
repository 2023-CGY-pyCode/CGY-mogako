import sys
from collections import deque
from enum import Enum
input = sys.stdin.readline
N = int(input())

dq =deque()
for _ in range(N):
    s = str(input()).strip()
    
    if s == "size":
        print(len(dq))
    elif s == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif s == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif s == "empty":
        print(1 if len(dq) == 0 else 0)
    elif s == "pop":
        if dq:            
            print(dq.popleft())
        else:
            print(-1)
    else:
        s1, s2 = tuple(map(str, s.split(" ")))
    
        if s1 == "push":
            dq.append(int(s2))
    
        
        