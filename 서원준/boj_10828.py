import sys
from collections import deque


n = int(sys.stdin.readline())
stack = deque()


for _ in range(n):
    tmp = sys.stdin.readline().split()
    
    if tmp[0] == "push":
        stack.append(tmp[1])
    
    elif tmp[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
 
    elif tmp[0] == "size":
        print(len(stack))
    
    elif tmp[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
     
    elif tmp[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

