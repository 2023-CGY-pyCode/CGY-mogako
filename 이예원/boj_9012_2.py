import sys
from collections import deque

n = int(sys.stdin.readline())

def ps_check(ps):
    stack = deque(ps)
    check_right = deque()
    while stack:
        cur = stack.pop()
        if cur == ')':
            check_right.append(cur)
        else:
            if len(check_right) == 0:
                return False
            else:
                check_right.pop()

    if len(check_right) != 0:
        return False
    else:
        return True

for _ in range(n):
    ps = list(sys.stdin.readline().rstrip())
    if ps_check(ps):
        print('YES')
    else:
        print('NO')
