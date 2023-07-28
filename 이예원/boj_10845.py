import sys
from collections import deque

n = int(sys.stdin.readline())
cmd_list = [sys.stdin.readline().split() for _ in range(n)]
q = deque()

for cmd in cmd_list:
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            p = q.popleft()
            q.appendleft(p)
            print(p)
    elif cmd[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            p = q.pop()
            q.append(p)
            print(p)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())