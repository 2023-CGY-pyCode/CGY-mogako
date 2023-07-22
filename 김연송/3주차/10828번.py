import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for i in range(N):
    A = list(sys.stdin.readline().split())

    if A[0] == 'push': # 정수 x를 스택에 넣기
        stack.append(A[1])
        
    elif A[0] == 'pop': # 스택 가장 위 정수를 빼고 없으면 -1
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif A[0] == 'top': # 가장 위에 있는 원소 반환
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) 

    elif A[0] == 'size': # 스택의 정수 수 출력
        print(len(stack))

    elif A[0] == 'empty': # 비어있으면 1, 아니면 0
        if len(stack) == 0:
            print(1)
        else:
            print(0)
