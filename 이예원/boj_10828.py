import sys
from collections import deque

n = int(sys.stdin.readline())
cmd_list = [sys.stdin.readline().split() for _ in range(n)]
q = deque()
for cmd in cmd_list:
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'top':
        if len(q) != 0:
            p = q.pop()
            print(p)
            q.append(p)
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) != 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'pop':
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)


